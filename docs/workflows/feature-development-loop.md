# Feature Development Loop

Feature development is the Incremental Design/Build loop specialized for net-new behavior.

```mermaid
flowchart LR
    R[Feature Outcome] --> S0[Stage 0]
    S0 --> A[System Design / Gate A]
    A --> B[Implementation Design / Gate B]
    B --> V1[Vertical Slice 1]
    V1 --> V2[Vertical Slice N]
    V2 --> VAL[Local + Clean Validation]
    VAL --> C[Gate C]
    C --> PR[PR-Ready Rollout]
```

## Requirements
Define outcomes, non-goals, compatibility, migration, security/reliability expectations, observability, and rollout constraints.

## Vertical slices
Prefer slices that traverse the real path end-to-end and can be deterministically validated. Avoid creating layers of disconnected scaffolding when a smaller working slice is possible.

## Rollout
For risky capabilities, include feature flag/canary/limited exposure, monitoring signals, rollback trigger, and rollback mechanism.

## Closure
Every acceptance criterion must trace to a design decision, implementation location, and observed validation evidence.
