# Design / Build Workflow

The canonical detailed lifecycle is [Incremental Design / Build Loop](./incremental-design-build-loop.md).

Use it for substantial features, behavioral fixes, refactors, and architectural changes.

At a minimum the lifecycle is:

```mermaid
flowchart LR
    S0[Stage 0] --> A[System Design]
    A --> GA[Gate A]
    GA --> B[Implementation Design]
    B --> GB[Gate B]
    GB --> I[Bounded Implementation]
    I --> V[Local / Clean Validation]
    V --> GC[Gate C]
    GC --> P[PR-Ready]
```

Do not maintain a second divergent design/build process in this document. The incremental loop is authoritative.
