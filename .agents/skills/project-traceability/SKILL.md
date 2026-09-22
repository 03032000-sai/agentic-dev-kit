---
name: project-traceability
description: Maintain durable stable-ID traceability from requirements through design, implementation, validation, critic findings, and residual risk across long-running changes.
---

# Project Traceability

## Stable IDs
Use:
- REQ-### requirements;
- DES-### system/design decisions;
- IMP-### implementation decisions;
- VAL-### tests/checks;
- FND-### critic findings;
- RSK-### residual risks.

## Forward trace
REQ → DES → IMP → file/symbol → VAL → observed evidence.

## Reverse trace
Detect implementation without requirement/design justification, tests tied only to removed behavior, stale documentation, and findings whose reviewed code later changed.

## Stage checks
Refresh traceability after Gate A, Gate B, each major implementation slice, Gate C, and candidate-SHA changes.

## Output
Traceability matrix, orphan/gap report, stale-link report, and residual-risk links.

Do not close a missing link using model confidence.
