# Multi-Repo Bootstrap Loop

```mermaid
flowchart TD
    I[Repository Inputs] --> V[Validate Names / Paths]
    V --> A[Attach or Clone Safely]
    A --> M[Inventory Branch / SHA / Remote]
    M --> D[Cross-Repo Discovery]
    D --> G[Dependency / Contract Graph]
    G --> E[Elect Anchor Repository]
    E --> C[Cross-Repo Artifacts + Integration Checklist]
```

## Safety
Never overwrite a non-empty checkout, discard local changes, or run a Git operation across wrapper and sub-repositories together.

## Discovery
Cross-repo relationships remain `inferred` unless supported by code/config/schema/deploy evidence.

## Documentation
Each application owns its local design docs. Shared cross-repo contracts and rollout artifacts live in the elected anchor repository.
