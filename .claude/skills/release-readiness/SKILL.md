---
name: release-readiness
description: Assess whether a candidate branch/change is ready for human release decision using traceability, clean-context validation, security review, observability, and rollback evidence.
---

# Release Readiness

Pin the exact candidate SHA. Verify acceptance traceability, diff scope, local and clean-context validation, security/dependency evidence, migration/compatibility, observability, rollback, documentation, and residual risks.

Publish a release packet with candidate SHA, evidence matrix, validation/security state, rollout/rollback, accepted exceptions, and fresh critic findings.

Output only READY FOR HUMAN DECISION or BLOCKED. Do not make the human merge/release decision.
