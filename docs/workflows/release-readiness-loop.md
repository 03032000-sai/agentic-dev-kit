# Release Readiness Loop

```mermaid
flowchart LR
    S[Pin Candidate SHA] --> T[Traceability]
    T --> D[Diff / Scope Review]
    D --> C[Clean Build + Tests]
    C --> SEC[Security / Dependency Review]
    SEC --> O[Observability + Rollback]
    O --> DOC[Documentation]
    DOC --> CR[Fresh Critic]
    CR -->|blocking| B[BLOCKED]
    CR -->|clear| H[READY FOR HUMAN DECISION]
```

## Candidate immutability
Review a specific SHA. If the branch changes after review, affected evidence must be refreshed.

## Required packet
- acceptance criteria → evidence;
- diff/scope summary;
- local/clean validation;
- security/dependency state;
- migration/backward compatibility;
- observability;
- rollout/rollback;
- documentation;
- residual risks/accepted exceptions.

## Human boundary
The workflow determines whether evidence is sufficient for a human decision. It does not autonomously release or merge.
