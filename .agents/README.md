# .agents

This is the canonical vendor-neutral agent asset surface.

## Skills

Reusable skills live under:

~~~text
.agents/skills/<skill>/SKILL.md
~~~

High-value skills also include:

~~~text
.agents/skills/<skill>/evals/eval.json
~~~

OpenAI Codex can use the root AGENTS.md plus these repository skills. Other tools may also read the canonical skills.

## Templates

Reusable governance artifacts live under ".agents/templates/":
- Change Brief
- durable checkpoint
- System Design
- Implementation Design
- critic findings
- traceability

## Runtime state

Runtime checkpoints and generated asset indexes may live under ".agents/" but are gitignored. Durable project documentation belongs in the host repository's approved docs paths, not in conversational memory.

## Authority

AGENTS.md is the repository-wide operating constitution. Skill files refine task-specific behavior but must not weaken its safety, gate, evidence, context, or Git rules.
