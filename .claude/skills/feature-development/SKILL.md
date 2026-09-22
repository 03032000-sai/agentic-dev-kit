---
name: feature-development
description: Deliver a new or materially extended capability through the full governed design-build lifecycle using vertically testable slices.
---

# Feature Development

Use `incremental-design-build` as the governing lifecycle.

## Feature-specific rules
- translate the request into explicit user/system outcomes and non-goals;
- identify compatibility constraints and migration needs early;
- design contracts before concrete implementation;
- prefer vertically testable slices that produce observable behavior;
- define feature flags/rollout controls when partial exposure is required;
- include failure paths, observability, and rollback in the design;
- maintain requirement → design → implementation → validation traceability.

## Slice strategy
Each slice should have:
- bounded behavior;
- deterministic acceptance check;
- minimal dependencies;
- reversible/low-risk rollout where feasible.

Do not create a "skeleton" that cannot be validated if a smaller end-to-end slice is possible.

## Completion
Gate C must show every acceptance criterion has implementation and evidence, docs are aligned, and rollout/rollback expectations are explicit.
