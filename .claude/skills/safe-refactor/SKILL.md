---
name: safe-refactor
description: Improve internal structure while preserving externally observable behavior through characterization evidence, bounded steps, and independent regression review.
---

# Safe Refactor

Define the behavior contract first. Identify public APIs/schemas, side effects, ordering/timing constraints, persistence behavior, and performance-sensitive paths. Add characterization tests where feasible.

Refactor in small steps, validating after each meaningful slice. Do not mix feature/bug work, silently change public interfaces, or weaken tests.

Finish with a fresh critic comparing before/after behavior, public contracts, diff scope, error behavior, and regression evidence. Gate C closes only when behavior preservation is credibly demonstrated.
