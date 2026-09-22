# Claude Code Project Instructions

`AGENTS.md` is the canonical engineering operating contract for this repository.

## Before substantial work
1. read `AGENTS.md`;
2. load the current durable checkpoint if one exists;
3. identify the appropriate workflow skill under `.claude/skills/`;
4. use specialist agents from `.claude/agents/` to preserve separation of powers;
5. keep authoring and fresh-context critique separate;
6. preserve evidence classes and deterministic validation across handoffs;
7. stop mutation if checkpoint/context integrity is lost;
8. require explicit approval for destructive, history-rewriting, credential-sensitive, production-impacting, push, or merge actions.

## Default workflow
For a non-trivial feature, fix, refactor, or behavior change use:

`/incremental-design-build <requirement>`

This workflow performs Stage 0 bootstrap, Change Brief + mechanical DoD, branch/checkpoint setup, progressive context scan, agent alignment, Gate A, Gate B, bounded implementation, local/clean validation, Gate C, traceability, and PR-ready handoff.

## Specialist entry points
- `/brownfield-bootstrap`
- `/knowledge-discovery`
- `/reverse-engineer-design`
- `/docs-code-alignment`
- `/safe-refactor`
- `/security-remediation`
- `/release-readiness`
- `/multi-repo-bootstrap`
- `/business-docs-loop`
- `/skill-scaffolding`
- `/agent-alignment`
- `/checkpoint-resume`
- `/clean-validation`
- `/project-traceability`
- `/test-oracle-design`
- `/observability-evidence`
- `/replay-debugging`

Use `/agents` to inspect available specialist agents.

## Context rule
Do not load the repository wholesale. Prefer instructions/checkpoint → indexes/manifests → targeted files → direct dependencies → deeper evidence only when needed.

Critics should receive fresh, minimal context rather than the author's full transcript.\n\nKeep active context below roughly 80%; checkpoint and compact/start fresh before crossing that threshold. Run at most four substantial implementation iterations in one session. Only one role owns repository mutation at a time, and Git Manager is the sole commit writer.
