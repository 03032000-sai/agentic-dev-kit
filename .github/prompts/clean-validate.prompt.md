---
description: Validate a candidate change from a safe clean repository context and produce reproducibility evidence.
---

Read `AGENTS.md` and invoke `clean-validation`.

Use a separate worktree/clone/container or equivalent clean environment; never destroy the active working tree. Pin candidate SHA, install from authoritative manifests/lockfiles, run required build/test/static/security/smoke checks, and report exact commands/discovery/results.

A clean-context failure remains blocking unless explicitly accepted.
