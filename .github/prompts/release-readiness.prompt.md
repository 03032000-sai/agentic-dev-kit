---
description: Build a release-readiness packet for an exact candidate SHA and identify blockers before human release/merge decision.
---

Read `AGENTS.md` and invoke `release-readiness`.

Pin the exact candidate SHA. Verify requirement traceability, diff scope, deterministic validation, clean-context reproducibility where required, security/dependency status, migration/compatibility, observability, rollback, documentation, and residual risks.

Use a fresh critic at the end. Report either BLOCKED or READY FOR HUMAN DECISION with the evidence packet. Do not merge or release automatically.
