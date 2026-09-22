# .claude

Claude Code adapters for the canonical agentic framework.

## Agents

Specialist subagents live under ".claude/agents/". Their role set is kept in parity with ".github/agents/" and validated in CI.

Use:

~~~text
/agents
~~~

to inspect available roles.

## Skills

".claude/skills/" is an exact mirror of canonical ".agents/skills/".

Do not hand-edit a Claude skill into a divergent version. Edit the canonical skill and run:

~~~bash
python3 scripts/sync_skills.py
~~~

## Project policy

Claude Code reads CLAUDE.md, which points back to the canonical AGENTS.md operating contract.

For substantial work, prefer "/incremental-design-build <requirement>" rather than a free-form code-first session.
