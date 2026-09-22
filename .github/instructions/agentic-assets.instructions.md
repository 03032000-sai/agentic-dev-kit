---
applyTo: ".github/agents/**,.github/prompts/**,.github/instructions/**,.agents/skills/**,.claude/agents/**,.claude/skills/**,AGENTS.md,CLAUDE.md"
---

# Agentic Asset Instructions

Treat agents, skills, prompts, and instructions as executable operating contracts.

- preserve valid frontmatter and routing-quality descriptions;
- avoid near-duplicate skills; extend canonical behavior instead;
- canonical reusable skills live in .agents/skills and are mirrored to .claude/skills;
- GitHub/Claude agent role sets should remain semantically aligned;
- substantial workflow skills need explicit inputs, outputs, safety/stop conditions, validation, and handoffs;
- high-value skills should include positive/negative eval fixtures;
- do not reduce detailed contracts to one-paragraph summaries;
- changes to Gate A/B/C, checkpoints, evidence classes, context limits, or Git authority must remain consistent across AGENTS.md, skills, prompts, and workflow docs.
