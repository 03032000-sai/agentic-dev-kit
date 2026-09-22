# Replay / Time-Travel Debugging

```mermaid
flowchart LR
    R[Failing Run + SHA] --> T[Ordered Timeline]
    T --> C[Last Known-Good Checkpoint]
    C --> P[Safe Replay]
    P --> D{State Divergence?}
    D -->|no| P
    D -->|yes| F[First Divergence]
    F --> O[Replay / Regression Oracle]
    O --> X[Responsible Fix Stage]
```

The goal is to find the **first** incorrect transition, not to explain only the final error.

Persisted run/checkpoint/event/tool evidence is authoritative. Missing history stays missing. If exact model replay is impossible, separate deterministic state/tool replay from a fresh nondeterministic model execution.

Original run evidence remains immutable, and replay must not re-trigger destructive external writes.
