---
name: incremental-design-build
description: Run the governed Stage 0 → Gate A → Gate B → implementation → Gate C lifecycle for substantial features, bug fixes, refactors, and behavioral changes.
---

# Incremental Design / Build

Use this skill when a change needs discovery, explicit design, bounded implementation, deterministic validation, and independent critique. Do not use the full loop for truly trivial edits.

## Invariants
- author ≠ sole verifier;
- system design ≠ implementation design;
- unknown ≠ success;
- mutable work happens on a dedicated branch;
- checkpoints preserve state across context/session changes;
- blocking findings stop progression;
- the workflow ends PR-ready, not silently merged;\n- only one role owns repository mutation at a time and Git Manager is the sole commit writer;\n- target <80% context usage; checkpoint/compact before crossing it;\n- maximum four substantial implementation iterations per session.

## Stage 0 — Fresh context
Invoke Repository Bootstrapper, then task-focused Repository Analyst.

Produce:
- repository/branch/SHA fingerprint;
- task evidence map;
- docs/code alignment notes;
- cross-repo dependencies when relevant;
- Change Brief;
- mechanical Definition of Done;
- validation plan;
- initial risks/unknowns.

Persist a checkpoint.

## Branch setup
Before implementation, use Git Manager to create/switch to a safe feature/fix branch. Do not discard existing work.

## Progressive context scan
Load instructions/checkpoint → indexes/manifests → task-relevant files → direct dependencies → deeper context only when required. Compact/checkpoint before stale context dominates.

## Agent-alignment round
Align active roles on goal, non-goals, requirements, evidence classes, constraints, DoD, open questions, and expected artifacts. Preserve disagreements as explicit open questions.

## Stage 1 — System Design
Invoke System Designer.

Required design:
- boundaries/responsibilities;
- contracts/interfaces;
- invariants;
- state/data/control flows;
- failure/recovery semantics;
- security/reliability/observability;
- compatibility constraints;
- alternatives/rejected options;
- unknowns;
- requirement traceability.

## Gate A
Invoke a fresh Design Critic. Provide only the Change Brief, system-design artifact, and minimum authoritative evidence.

- BLOCKING → return to System Designer.
- IMPORTANT → resolve or explicitly record.
- ADVISORY → may remain as recommendation.
- PASS → proceed.

Checkpoint approved Gate A artifact.

## Stage 2 — Implementation Design
Invoke Implementation Designer.

Required plan:
- exact files/modules/symbols;
- APIs/schemas/state;
- dependencies;
- error/retry contracts;
- migration/compatibility;
- tests;
- telemetry;
- rollout/rollback;
- exact validation commands;
- ordered implementation slices.

## Gate B
Invoke a fresh Implementation Plan Critic.

If the problem is architectural, reopen Gate A. Otherwise return blocking findings to Implementation Designer. Only proceed when implementation can occur without architectural invention.

Checkpoint approved Gate B artifact.

## Stage 3 — Bounded implementation
Invoke Implementer.

For each slice:
1. reload only necessary current context;
2. implement smallest approved slice;
3. add/update tests;
4. run targeted local validation;
5. record changed files/results;
6. checkpoint;
7. decide continue/escalate/stop.

Do not continue indefinitely in one context window. Run at most **four substantial implementation iterations per session**. Checkpoint and continue from fresh context earlier if active context approaches **80%** or context quality degrades.

## Local validation
Invoke Local Operator for formatter/linter/type/static checks, targeted and broad tests, builds/packages, scanners, and smoke checks as appropriate.

Exact commands + results are evidence.

## Clean-context validation
For substantial/release-bound changes invoke Clean-Repo Operator. Validate from clean state without destroying the user's working tree.

## Gate C
Invoke fresh Implementation Critic with:
- Change Brief + DoD;
- approved designs;
- actual diff;
- local/clean validation evidence;
- docs;
- residual risks.

Blocking findings route back to the responsible stage.

## Completion
Invoke Traceability Analyst, then Git Manager.

Produce:
- requirement → design → implementation → test/evidence matrix;
- branch/status/diff summary;
- validation summary;
- open risks/exceptions;
- proposed commit/PR message;
- recommended human action.

Do not merge automatically.

## Degraded mode
If checkpoint persistence fails, required evidence is inaccessible, or context cannot be trusted: stop mutation and switch to read-only planning until durable state is restored.
