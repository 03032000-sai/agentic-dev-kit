---
name: oauth2-pkce-integration
description: Implement OAuth2 Authorization Code flow with PKCE for a Git-hosting or identity provider.
---

# OAuth2 + PKCE Integration
Implement the Authorization Code flow with PKCE: generate a code verifier/challenge pair, send the challenge in the authorization request, exchange the code plus verifier for tokens server-side. Store tokens server-side or in an httpOnly cookie — never in `localStorage` or a client-readable cookie. Implement refresh-token rotation and handle expiry by re-authenticating, not by silently failing. Scope requested permissions to the minimum the integration needs.
