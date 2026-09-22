# GitHub Copilot Repository Instructions

The canonical cross-tool policy is `/AGENTS.md`.

For substantial tasks:
- read `AGENTS.md` before editing;
- use repository evidence before assumptions;
- keep discovery, system design, implementation design, implementation, and critique separate;
- use `.github/agents/` for specialist roles;
- use `.agents/skills/` for reusable task workflows;
- use `.github/prompts/` for repeatable entry points;
- run deterministic validation before declaring completion;
- surface unknowns and failed checks explicitly;
- require human approval before destructive, irreversible, security-sensitive, or production-impacting operations.

Prefer small, reviewable changes over broad rewrites.
