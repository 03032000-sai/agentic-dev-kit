---
name: skill-scaffolding
description: Create or extend a grounded repository skill with routing metadata, evidence, examples, and behavioral eval fixtures.
---

# Skill Scaffolding

## Preconditions
Before creating a skill:
1. confirm the tool/technology/workflow is actually used or intentionally being introduced;
2. search existing skills for overlap;
3. prefer extending an existing skill to creating a near-duplicate.

## Skill contract
Each skill must include:
- canonical `name`;
- routing-quality `description` explaining when to use it;
- mission/scope;
- concrete operating rules;
- safety/stop conditions;
- validation expectations;
- conflict/precedence rules when relevant;
- examples only when they add behavioral clarity.

## Grounding
Guidance must be grounded in repository conventions or authoritative technology behavior. Do not fabricate package names, commands, endpoints, or policy.

## Evals
Add at least:
- positive trigger case;
- negative trigger case;
- expected required behavior;
- prohibited behavior;
- simple output assertions.

## Cross-tool parity
Canonical skill lives in `.agents/skills/<name>/`. Mirror the complete directory to `.claude/skills/<name>/` using the repository sync mechanism.

## Completion
Run structural validation and skill eval validation. A skill is not complete merely because `SKILL.md` exists.
