---
name: release-readiness
description: Assess whether a candidate branch/change is ready for human release decision using traceability, clean-context validation, security review, observability, and rollback evidence.
---

# Release Readiness

## Preconditions
Identify the exact candidate branch/commit SHA. Do not assess a moving target.

## Review dimensions
1. **Acceptance:** every required criterion maps to implementation and evidence.
2. **Scope:** diff matches approved Change Brief/design.
3. **Validation:** relevant unit/integration/E2E/build checks pass.
4. **Clean reproducibility:** clean-context validation succeeds when required.
5. **Security/dependencies:** required scans/reviews are complete and discovery scope is credible.
6. **Migration/compatibility:** schema/data/API changes have rollout/backward-compatibility evidence.
7. **Observability:** success/failure signals and dashboards/logs/alerts exist where needed.
8. **Rollback:** trigger, mechanism, data implications, and owner are explicit.
9. **Documentation:** user/operator/design docs are current.
10. **Residual risk:** accepted exceptions are explicit and human-owned.

## Output
Produce a release packet:
- candidate SHA;
- requirement/evidence matrix;
- validation table;
- security status;
- migration/rollout notes;
- rollback plan;
- residual-risk register;
- fresh critic findings;
- final status: READY FOR HUMAN DECISION or BLOCKED.

Do not make the human release/merge decision yourself.
