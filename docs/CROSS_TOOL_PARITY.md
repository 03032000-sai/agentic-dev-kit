# Cross-Tool Parity

The framework has one conceptual operating model with tool-native adapters.

| Concept | GitHub Copilot | Claude Code | OpenAI Codex |
|---|---|---|---|
| Canonical repository policy | AGENTS.md + copilot-instructions | AGENTS.md + CLAUDE.md | AGENTS.md |
| Specialist roles | .github/agents/*.agent.md | .claude/agents/*.md | roles defined by AGENTS.md and invoked through skills/instructions |
| Canonical reusable skills | .agents/skills | exact mirror in .claude/skills | .agents/skills |
| Workflow launchers | .github/prompts/*.prompt.md | slash-invokable skills | explicit skill invocation |
| Shared contracts/templates | docs/contracts + .agents/templates | same | same |
| Evals | .agents/skills/*/evals | mirrored | canonical |
| Runtime checkpoint convention | .agents/checkpoints/<branch>/ | same repository state | same repository state |

## Parity invariants

1. GitHub and Claude custom-agent filename sets must match.
2. Claude skill directories are byte-for-byte mirrors of canonical ".agents/skills".
3. Gate A/B/C semantics are defined once in AGENTS.md / docs/contracts and are not reinterpreted by adapters.
4. The same evidence classes, <80% context ceiling, four-iteration/session bound, single-writer commit rule, and checkpoint fail-safe apply across tools.
5. Tool-specific prompt syntax may differ, but authority boundaries do not.

## Direct stage mapping

| Stage | Copilot prompt | Claude/Codex capability |
|---|---|---|
| Stage 0 | bootstrap-repo | Repository Bootstrapper / repo-discovery |
| Alignment | agent-alignment | agent-alignment skill |
| System Design | system-design | System Designer / system-design |
| Gate A | gate-a-review | Design Critic |
| Implementation Design | implementation-design | Implementation Designer / implementation-design |
| Gate B | gate-b-review | Implementation Plan Critic |
| Implementation | implement-feature | Implementer / Implementation Executor |
| Local validation | local-validate | Local Operator |
| Clean validation | clean-validate | clean-validation / Clean-Repo Operator |
| Gate C | gate-c-review | Implementation Critic |
| Traceability | project-traceability | project-traceability |
| Git handoff | git-handoff | Git Manager / Git Repo Manager |
| Context rollover | context-compact | context-governance |
| Replay debugging | replay-debugging | replay-debugging |

CI is the enforcement mechanism for structural parity; this document explains the intended semantic parity.
