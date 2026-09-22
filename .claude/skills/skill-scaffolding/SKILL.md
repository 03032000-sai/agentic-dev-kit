---
name: skill-scaffolding
description: Author a new grounded skill (and its eval fixture) for a tool or technology this repository actually uses.
---

# Skill Scaffolding
Before authoring a new skill, confirm the tool/technology is actually present in this repository (config file, dependency manifest, CI step) — never scaffold a skill for a hypothetical stack. Ground every guidance line in a cited real file from this repo. Write the skill in the existing dense, single-paragraph style used by other skills in `.agents/skills/`. Pair it with a minimal eval fixture (a representative task plus an expected-good-output check) so the skill's guidance is verifiable, not just aspirational. Do not scaffold a skill that duplicates an existing one — extend the existing skill instead.
