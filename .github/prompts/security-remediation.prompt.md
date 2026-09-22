---
description: Remediate a security finding with evidence confirmation, least privilege, deterministic rescanning, and fresh security critique.
---

Read `AGENTS.md` and invoke `security-remediation`.

Preserve the exact finding/scanner scope. Confirm/reproduce where possible, add reachability/exploitability context without overstating certainty, design the smallest durable fix, and pause for explicit human review when authn/authz, crypto, secrets, trust boundaries, or production permissions change.

Require regression evidence, rerun the originating scanner with valid discovery, and finish with a fresh Security Reviewer/critic. Do not call a zero-discovery scan clean.
