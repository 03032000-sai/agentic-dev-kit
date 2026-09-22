# Architecture Analysis

```mermaid
flowchart LR
    E[Repository Evidence] --> B[Boundaries / Components]
    B --> C[Contracts / State]
    C --> F[Flows / Failures]
    F --> X[Security / Reliability / Observability]
    X --> D[Evidence-backed Diagrams]
    D --> O[Architecture Model + Risks + Unknowns]
```

Architecture analysis describes current structure. Redesign requires a separate System Design stage and Gate A.
