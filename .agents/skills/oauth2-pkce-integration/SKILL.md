---
name: oauth2-pkce-integration
description: Design and implement OAuth 2.x Authorization Code + PKCE integrations with least privilege and explicit state/redirect protections.
---

# OAuth2 + PKCE Integration

## Design
Identify:
- authorization server;
- client type;
- redirect URIs;
- scopes actually required;
- authorization/token endpoints from authoritative configuration;
- token storage/refresh behavior;
- logout/revocation expectations.

## PKCE
Generate a high-entropy code verifier per authorization attempt and derive an S256 code challenge. Bind the verifier to the browser/session state that initiated the request.

## CSRF/session binding
Use and validate `state`; do not accept callback state that was not issued for the active flow. Treat redirect URI matching as exact according to provider rules.

## Scope rule
Request the minimum scopes required by the use case. Broad example scopes from documentation do not override least privilege.

## Secrets
Public clients must not rely on a client secret for confidentiality. Never commit secrets, tokens, or verifiers.

## Validation
Test success, denied consent, invalid state, missing/expired verifier, callback replay, refresh failure, and logout/revocation behavior as applicable.
