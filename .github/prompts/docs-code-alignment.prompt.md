---
description: Classify and resolve documentation/code drift using explicit source-of-truth rules and evidence.
---

Read `AGENTS.md` and invoke `docs-code-alignment`.

Extract material documentation claims, map each to code/config/tests/approved-design evidence, classify drift, and decide correction direction explicitly. Do not invent historical rationale or silently change code to make docs true.

Use a fresh Findings Critic and report source SHA, corrected/proposed docs, real design divergences, and unresolved gaps.
