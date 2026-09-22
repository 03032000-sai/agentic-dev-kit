---
name: clean-validation
description: Prove that a candidate change builds, tests, scans, and behaves from a clean repository context without destroying the developer working tree.
---

# Clean Validation

## Goal
Detect hidden dependencies on caches, generated residue, untracked files, local environments, or unstated setup.

## Safe environment
Prefer:
- separate Git worktree;
- temporary clone;
- disposable container;
- CI-equivalent clean environment.

Never clean/reset the user's active working tree merely to simulate cleanliness.

## Validate as applicable
- candidate commit SHA;
- dependency installation from authoritative manifests/lockfiles;
- generated-file/codegen expectations;
- format/lint/type/static checks;
- unit/integration/E2E tests;
- build/package;
- security/dependency scans;
- startup/smoke checks;
- required environment assumptions.

## Evidence
Capture environment, exact commands, exit results, discovered test/package counts, artifacts, and failures.

## Closure
Clean-context failure blocks release-ready status unless explicitly accepted by a human with residual risk recorded.
