---
description: Refactor implementation safely while preserving externally observable behavior.
---

Read `AGENTS.md` and invoke `safe-refactor`.

Before edits, define the behavior contract and characterization evidence. Produce a bounded refactor plan with explicit non-goals. Implement in small validated slices and do not mix feature/bug work into the same refactor.

Finish with broader regression/clean validation when warranted and a fresh Gate C critic comparing public contracts, side effects, error behavior, diff scope, and tests.
