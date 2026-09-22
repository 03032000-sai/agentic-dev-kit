# Gate Contract

Gates are explicit readiness decisions, not stylistic review checkpoints.

## Gate A — System Design Readiness

### Required inputs
- Change Brief + mechanical Definition of Done
- Stage 0 evidence map
- system design artifact
- relevant constraints and risks

### Pass criteria
- boundaries and responsibilities are explicit;
- contracts/interfaces are defined;
- invariants are testable or observable;
- state/data/control flows are coherent;
- failure behavior is described;
- security/reliability/observability are addressed;
- unknowns and rejected alternatives are visible;
- no unresolved `BLOCKING` critic findings remain.

### Failure behavior
Return to System Designer with findings. Do not begin concrete implementation design.

## Gate B — Implementation Design Readiness

### Required inputs
- approved Gate A artifacts
- implementation design
- repository evidence

### Pass criteria
- exact files/components are identified;
- APIs/schemas/state changes are concrete;
- ownership and dependencies are explicit;
- error contracts and compatibility behavior are defined;
- unit/integration/E2E coverage is planned;
- telemetry is planned;
- rollout/rollback is credible;
- validation commands are executable;
- implementation can proceed without architectural invention;
- no unresolved `BLOCKING` findings remain.

### Failure behavior
Return to Implementation Designer. If the problem is architectural, reopen Gate A.

## Gate C — Implementation + Validation Closure

### Required inputs
- Change Brief/DoD
- approved designs
- actual diff
- local validation
- clean validation when required
- documentation changes
- residual-risk register

### Pass criteria
- implementation matches approved scope/design;
- each acceptance criterion maps to credible evidence;
- validation failures are resolved or explicitly accepted by the human;
- clean-context reproducibility is proven when required;
- blocking critic findings are closed;
- documentation is aligned;
- Git/checkpoint state is coherent.

### Failure behavior
Route back to the responsible stage. Do not declare completion.
