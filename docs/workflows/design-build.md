# Design / Build Workflow

Use for non-trivial features and architectural changes.

1. **Discover** — gather only the evidence needed for the task.
2. **System Design** — define boundaries, contracts, invariants, flows, failure behavior, and non-functional requirements.
3. **Gate A: Critique** — independently review the system design.
4. **Implementation Design** — map approved design to files, APIs, schemas, tests, telemetry, rollout, and rollback.
5. **Gate B: Critique** — review feasibility, completeness, and traceability.
6. **Implement** — change only approved scope.
7. **Gate C: Validate** — run deterministic checks and independent review.
8. **Complete** — request human approval when the change crosses a configured risk boundary.
