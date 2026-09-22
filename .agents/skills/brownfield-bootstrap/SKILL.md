---
name: brownfield-bootstrap
description: Establish a trustworthy current-state baseline for an unfamiliar existing repository before any substantial change.
---

# Brownfield Bootstrap

Use when the repository is unfamiliar, poorly documented, or likely to contain documentation/code drift.

## Flow
1. Repository Bootstrapper captures repo/branch/SHA, instructions, stack, build/test/deploy, docs, and working-tree state.
2. Repository Analyst maps task-relevant entry points, boundaries, state, integrations, and tests.
3. Reverse-engineer current system design.
4. Reverse-engineer current implementation design.
5. Docs-Code Aligner compares documented claims with executable evidence.
6. Fresh Map/Findings Critics review the baseline.
7. Produce current-state baseline artifacts and validation-command inventory.
8. Only then enter feature/bug/refactor design-build.

## Source-of-truth rule
For current behavior, executable code/config/tests are stronger than stale docs unless an explicitly approved target design supersedes them.

## Output
- repo fingerprint;
- current system design;
- current implementation map;
- docs/code drift report;
- test/build/deploy command inventory;
- unknowns/risks;
- source SHA;
- recommended next workflow.

Do not mutate product code during the pre-loop.
