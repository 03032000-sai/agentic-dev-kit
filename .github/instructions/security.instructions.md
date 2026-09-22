---
applyTo: "**/*"
---

# Security Instructions

- preserve least privilege for users, services, agents, tools, and CI;
- never commit secrets, tokens, credentials, or private keys;
- do not weaken authentication/authorization/cryptography to make tests pass;
- identify trust boundaries for security-sensitive changes;
- treat fail-open behavior as an explicit design decision, not a convenience;
- deterministic scanner evidence outranks model confidence;
- zero expected packages/files/rules scanned is failure, not a clean result;
- enrichment such as KEV/EPSS adds context but does not erase source findings;
- authn/authz, crypto, secret-handling, trust-boundary, and production-permission fixes require explicit human review.
