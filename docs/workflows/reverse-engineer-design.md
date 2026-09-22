# Reverse-Engineer Design Workflow

```mermaid
flowchart LR
    E[Executable Evidence] --> A[Abstract Current Design]
    A --> I[Concrete Implementation Map]
    I --> M[Evidence Links]
    M --> C[Fresh Critics]
    C --> O[Current-State Baseline]
```

The workflow deliberately reconstructs **current state**, not an idealized architecture.

Keep rationale separate from structure: code may confirm WHAT the system does without proving WHY it was designed that way.
