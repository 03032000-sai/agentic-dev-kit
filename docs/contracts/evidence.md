# Evidence Contract

## Evidence classes

- **confirmed** — directly supported by code, configuration, tests, generated artifacts, deterministic tool output, or an authoritative runtime response.
- **documented** — asserted in documentation but not independently verified.
- **inferred** — reasoned from evidence but not explicitly established.
- **unknown** — insufficient evidence.

## Claim envelope

```yaml
claim_id:
claim:
status: confirmed | documented | inferred | unknown

source:
  repository:
  path:
  symbol:
  line_range:
  commit_sha:

validation:
  command:
  result:

notes:
```

## Rules

- A model statement is not evidence by itself.
- A failing or incomplete scan cannot support a clean claim.
- If a tool discovers zero expected inputs (for example, zero packages), classify the validation as failed/blocked rather than "no findings."
- Documentation may support `documented`, not automatically `confirmed`.
- Inference must remain visibly labeled through downstream artifacts.
