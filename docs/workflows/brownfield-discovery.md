# Brownfield Discovery

Brownfield discovery establishes a trustworthy current-state model before design changes begin.

```mermaid
flowchart TD
    B[Repository Bootstrap] --> R[Focused Repository Analysis]
    R --> S[Current System Design]
    S --> I[Current Implementation Design]
    I --> D[Docs-Code Alignment]
    D --> C[Fresh Critics]
    C --> BL[Baseline at Source SHA]
    BL --> N[Normal Change Workflow]
```

## Required baseline
- repository fingerprint and source SHA;
- build/test/deploy commands;
- architecture boundaries/contracts;
- implementation file/symbol map;
- data/state/integration paths;
- relevant tests;
- docs/code drift;
- confirmed/documented/inferred/unknown register.

Do not infer historical intent from implementation structure alone.
