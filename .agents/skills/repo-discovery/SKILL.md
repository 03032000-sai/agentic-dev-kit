---
name: repo-discovery
description: Discover an unfamiliar repository progressively and produce an evidence map. Use for brownfield analysis, unfamiliar codebases, architecture discovery, or before non-trivial changes. Do not use when the relevant files and behavior are already known.
---

# Repository Discovery
1. Read repository-level instructions.
2. Inspect root structure and high-signal metadata.
3. Identify languages, package managers, build/test systems, and deployment configuration.
4. Read architecture/docs only as needed.
5. Locate likely entry points and dependency boundaries.
6. Trace only task-relevant paths.
7. Locate tests that encode current behavior.
8. Produce an evidence map with paths, symbols, confirmed behavior, tests, constraints, inferences, and unknowns.
9. Stop when enough evidence exists for the next stage.

Do not modify source code while using this skill.
