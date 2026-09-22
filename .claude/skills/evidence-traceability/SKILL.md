---
name: evidence-traceability
description: Build and verify requirement → design → implementation → validation traceability using explicit evidence classes.
---

# Evidence Traceability

For each requirement assign a stable ID and map:

requirement → system-design decision → implementation-design decision → files/symbols → tests/checks → observed evidence.

Classify claims:
- confirmed;
- documented;
- inferred;
- unknown.

Flag:
- requirement without implementation;
- implementation without requirement/design justification;
- test that does not demonstrate the claimed behavior;
- documentation that no longer matches code;
- validation claim without command/output;
- accepted risk without explicit owner/rationale;
- inferred fact presented as confirmed.

Do not "close" a trace gap with model confidence. Missing evidence remains a gap.
