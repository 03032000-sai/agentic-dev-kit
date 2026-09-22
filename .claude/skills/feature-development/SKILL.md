---
name: feature-development
description: Deliver a new or materially extended capability through the full governed design-build lifecycle using vertically testable slices.
---

# Feature Development

Use `incremental-design-build` as the governing lifecycle. Translate the request into explicit outcomes/non-goals, handle compatibility/migration early, design contracts before code, and implement vertically testable slices with deterministic acceptance checks.

Include failure paths, observability, rollout/rollback, and requirement-to-evidence traceability. Prefer a small end-to-end behavior over an untestable skeleton.

Gate C closes only when every acceptance criterion maps to implementation and evidence and material docs are current.
