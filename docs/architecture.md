# Architecture

`agentic-dev-kit` separates durable repository knowledge from tool-specific adapters.

## Layers

1. **Canonical policy** — `AGENTS.md`
2. **Task skills** — `.agents/skills/`
3. **Tool adapters**
   - GitHub Copilot: `.github/`
   - Claude Code: `.claude/`
   - Codex: `AGENTS.md` + `.agents/skills/`
4. **Workflow documentation** — `docs/workflows/`
5. **Deterministic validation** — `scripts/validate_repo.py`

## Role boundaries

| Role | Reads | Writes | Primary output |
| --- | --- | --- | --- |
| Repository Analyst | repo/docs/tests | none | evidence map |
| System Designer | evidence + requirements | design docs | abstract design |
| Implementation Designer | approved design + evidence | plan docs | technical plan |
| Implementer | approved plan + source | source/tests | code change |
| Critic | artifact + requirements + evidence | none by default | findings |
| Git Manager | Git state | Git metadata | branch/commit summary |

## Future runtime layer

A later release may implement the workflow with LangGraph and AWS Strands while preserving these contracts.
