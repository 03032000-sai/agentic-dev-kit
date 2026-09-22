# Knowledge Discovery Loop

The canonical workflow is documented in [knowledge-discovery.md](./knowledge-discovery.md).

```mermaid
flowchart LR
    Q[Question] --> D[Progressive Evidence Discovery]
    D --> M[Claim / Evidence Map]
    M --> S[Synthesis]
    S --> C[Fresh Critic]
    C --> A[Answer + Gaps + Source SHA]
```

Use confirmed/documented/inferred/unknown classifications and keep WHAT separate from unsupported WHY.
