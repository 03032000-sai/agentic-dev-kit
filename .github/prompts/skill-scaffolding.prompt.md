---
description: Create or extend a grounded repository skill with routing metadata, conflict rules, validation guidance, and positive/negative eval fixtures.
---

Read `AGENTS.md` and invoke `skill-scaffolding`.

First confirm the technology/workflow is actually used or intentionally being introduced and search for overlapping skills. Prefer extending an existing skill over creating a duplicate.

Create/update the canonical `.agents/skills/<name>/` skill with routing-quality frontmatter, concrete operating/safety/validation rules, and `evals/eval.json` containing positive/negative trigger cases plus required/forbidden behaviors.

Mirror through the repository skill-sync mechanism and run structural/eval validation.
