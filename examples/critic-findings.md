# Critic Findings — Example Gate A

### FND-001 — Dependency failure semantics are undefined
- Severity: BLOCKING
- Affected artifact: system design / failure behavior
- Problem: the design does not decide whether inability to evaluate quota fails open or fails closed.
- Evidence: the system design explicitly leaves the policy unresolved.
- Impact: implementation would otherwise invent security/availability behavior.
- Required resolution: approve explicit failure semantics before Gate A passes.

## Gate recommendation
FAIL until FND-001 is resolved.
