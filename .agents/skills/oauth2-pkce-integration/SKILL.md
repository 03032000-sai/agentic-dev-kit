---
name: oauth2-pkce-integration
description: Use when implementing GitLab (or other Git-hosting/identity-provider) OAuth2 sign-in with PKCE (Proof Key for Code Exchange), configuring sign-in for a self-hosted or corporate GitLab instance, storing and refreshing OAuth tokens, or adding GitLab authentication to a web application.
---

# OAuth2 + PKCE Integration

Implement GitLab sign-in using OAuth2 with Proof Key for Code Exchange (PKCE) in a web application.

## Overview
This skill provides a complete workflow for: setting up GitLab OAuth2 authentication (PKCE flow); supporting both GitLab.com and self-hosted/corporate instances; exchanging authorization codes for access tokens; managing token storage and refresh; handling scope permissions for API access.

Reference: the GitLab OAuth2 PKCE documentation for your GitLab version.

## Prerequisites
- **GitLab OAuth application:** register an OAuth application in your GitLab instance.
- **Credentials file:** a `gitlab_tokens.md` (or equivalent secret store) in the workspace root containing the GitLab base URL, application ID, application secret, and required scopes.
- **`.gitignore` entry:** ensure the credentials file is gitignored (do NOT commit tokens).

## Step-by-Step Implementation

**Phase 1 — Credential Configuration** (backend service environment or config module)
- Read the credentials file. Extract: GitLab base URL (e.g. `https://gitlab.example.com/` or `https://gitlab.com/`); application ID; secret; scopes list (recommended: `api`, `read_user`, `read_api`, `openid`, `profile`, `email`).
- Validate all required fields are present.
- Store in environment variables or secure config (never hardcode in source): `GITLAB_BASE_URL`, `GITLAB_CLIENT_ID`, `GITLAB_CLIENT_SECRET`, `GITLAB_SCOPES`, `GITLAB_REDIRECT_URI` (must match the registered redirect URI in GitLab).
- Quality check: confirm the base URL ends with `/` and is reachable.

**Phase 2 — PKCE Generation Utility** (shared authentication utilities)
Language-specific libraries: Python — `secrets` module + base64 encoding; JavaScript/TypeScript — `crypto` module or `crypto-js`; else — a platform-provided cryptographic library.
Implement or import a function that: generates a random `code_verifier` (43–128 characters, unreserved URI characters); creates a SHA256 hash of the verifier; base64-URL encodes the hash (`code_challenge`); returns both `code_verifier` and `code_challenge`.
Security note: never reuse a `code_verifier`. Generate a new pair for each auth attempt.

**Phase 3 — Authorization URL Construction** (frontend or session initialization)
```
{GITLAB_BASE_URL}/oauth/authorize?
  client_id={APPLICATION_ID}
  &redirect_uri={REDIRECT_URI}
  &response_type=code
  &code_challenge={CODE_CHALLENGE}
  &code_challenge_method=S256
  &scope={SPACE_SEPARATED_SCOPES}
  &state={STATE_TOKEN}
```
Include a `state` parameter for CSRF protection (random token, stored in session). Always use `code_challenge_method=S256`. URL-encode all parameter values.

**Phase 4 — Authorization Code Callback** (redirect URI callback endpoint)
Verify the `state` parameter matches the one stored in session. Extract `code` (valid ~10 minutes). If an `error` parameter is present, handle gracefully (user denied, invalid scope, etc.). Do NOT proceed without state validation.

**Phase 5 — Token Exchange** (backend service — must be server-to-server, never exposed from frontend)
```
POST {GITLAB_BASE_URL}/oauth/token
Content-Type: application/x-www-form-urlencoded

grant_type=authorization_code
&client_id={APPLICATION_ID}
&client_secret={CLIENT_SECRET}
&code={AUTHORIZATION_CODE}
&redirect_uri={REDIRECT_URI}
&code_verifier={CODE_VERIFIER}
```
Response (on success): `access_token`, `token_type`, `expires_in`, `refresh_token`, `scope`.
Error handling: `invalid_grant` (code expired/used → restart auth flow); `invalid_client` (bad credentials → check credentials store); `invalid_redirect_uri` (mismatch → verify in GitLab OAuth app settings).

**Phase 6 — Token Storage & Session Management.** Do NOT store tokens in browser `localStorage` (XSS risk). Store securely: `access_token` (used as `Authorization: Bearer {token}`); `refresh_token`; `expires_in`; `scope`. Link tokens to the authenticated user ID, encrypt at rest, set secure `HttpOnly` cookies for session tracking.

**Phase 7 — API Calls with Access Token**
```
GET {GITLAB_BASE_URL}/api/v4/user
Authorization: Bearer {access_token}
```
All API scopes from the credentials store apply to requests. A missing scope returns 403.

**Phase 8 — Token Refresh (optional).** When the access token is nearing expiration or a 401 is returned:
```
POST {GITLAB_BASE_URL}/oauth/token
Content-Type: application/x-www-form-urlencoded

grant_type=refresh_token
&client_id={APPLICATION_ID}
&client_secret={CLIENT_SECRET}
&refresh_token={REFRESH_TOKEN}
```
Automatic refresh strategy: check expiration before each API call; refresh proactively within 5 minutes of expiry; on 401, refresh and retry once.

**Phase 9 — Sign-Out / Token Revocation.**
```
POST {GITLAB_BASE_URL}/oauth/revoke
Content-Type: application/x-www-form-urlencoded

client_id={APPLICATION_ID}
&client_secret={CLIENT_SECRET}
&token={access_token}
```
After revocation: delete tokens from the session store, clear session cookies, redirect to home/login.

## Configuration Checklist
- Credentials file present with correct values and gitignored.
- `GITLAB_BASE_URL`, `GITLAB_CLIENT_ID`, `GITLAB_CLIENT_SECRET` loaded into environment.
- `GITLAB_REDIRECT_URI` matches the registered URI in the GitLab OAuth app.
- PKCE generation utility implemented and tested.
- Authorization URL construction properly URL-encodes parameters.
- State token validated before exchanging code for token.
- Token exchange happens on backend only (never expose the client secret to frontend).
- Access tokens stored securely (encrypted, server-side, `HttpOnly` cookies).
- Error handling implemented for expired codes, invalid grants, network failures.
- API calls include the `Authorization: Bearer {token}` header.
- Token refresh logic (or at minimum, restart-auth-flow on 401).

## Common Pitfalls
- **Client secret exposed to frontend:** never send `CLIENT_SECRET` to the browser. Token exchange must be server-to-server.
- **Missing PKCE parameters:** always include `code_challenge` and `code_verifier` — without them, you're vulnerable to authorization-code interception.
- **State parameter skipped:** omitting `state` allows CSRF attacks; always validate before exchanging code.
- **Hard-coded credentials:** never commit credentials; always use environment variables or gitignored files.
- **Wrong base URL for a self-hosted instance:** ensure a trailing slash and correct URL in all requests.
- **Scope mismatch:** request only needed scopes; a 403 means a required scope is missing from the token request.
- **Token expiration not handled:** implement refresh or re-auth logic, otherwise users get random 401 errors after ~1 hour.

## Implementation Patterns by Framework
**Python (FastAPI / Flask):** use `requests` for HTTP calls; store tokens in server-side sessions (Redis, database); use `httponly=True` cookies for the session ID.
**JavaScript/TypeScript (Express/Next.js):** use `node-fetch`/`axios`; use secure session middleware (`express-session` + store); frontend calls a backend endpoint to initiate the OAuth flow.
**Both:** PKCE code generation via a crypto module + base64 encoding; token storage in an encrypted database table + session association; catch network errors, invalid credentials, and scope misses.

## Testing
- Manual auth flow: start from sign-in, complete redirect, verify token received.
- API call validation: use the token to call the API, confirm 200 OK.
- Token expiration: wait for (or mock) expiry, verify refresh works.
- Error scenarios: deny permissions, provide an invalid code, test network failures.
- Self-hosted instance: test against your organization's GitLab URL if applicable.
