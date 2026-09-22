# Usage Guide

The repository is designed to be used directly from chat. No orchestration server is required.

## Pick the workflow first

| Need | Workflow |
|---|---|
| substantial feature / behavior change | `incremental-design-build` |
| new feature specifically | `feature-development` |
| non-trivial bug | `bugfix` |
| unfamiliar repository | `brownfield-bootstrap` |
| architecture/current-state question | `knowledge-discovery` or `architecture-analysis` |
| reconstruct design from code | `reverse-engineer-design` |
| docs drift | `docs-code-alignment` |
| behavior-preserving refactor | `safe-refactor` |
| security finding | `security-remediation` |
| pre-release evidence | `release-readiness` |
| multiple repositories | `multi-repo-bootstrap` |
| business-facing docs from code | `business-docs-loop` |

## GitHub Copilot

Use the Agent picker for specialist roles such as System Designer, Implementer, Design Critic, or Git Manager.

Use prompt files for complete workflows. Examples:

```text
Run incremental-design-build for: Add rate limiting to the public API.
Run bugfix for: Duplicate events are creating two records.
Run brownfield-bootstrap for this repository before we change anything.
```

## Claude Code

Claude reads `CLAUDE.md` and the canonical `AGENTS.md`.

Examples:

```text
/incremental-design-build Add rate limiting to the public API.
/bugfix Fix duplicate event processing.
/knowledge-discovery Explain the authentication flow.
/business-docs-loop Create business-readable documentation for this service.
```

Use `/agents` to inspect specialist agents.

## OpenAI Codex

Codex uses the root `AGENTS.md` and canonical skills under `.agents/skills/`.

Examples:

```text
$incremental-design-build Add rate limiting.
$bugfix Fix duplicate notifications.
$knowledge-discovery Explain authentication.
```

## What a good run looks like

A substantial run should visibly move through:
1. Stage 0 context;
2. Change Brief + DoD;
3. safe branch/checkpoint;
4. Gate A;
5. Gate B;
6. bounded implementation;
7. local validation;
8. clean validation when required;
9. Gate C;
10. traceability + PR-ready handoff.

If the assistant jumps straight from requirement to code, ask it to restart with the canonical workflow.

## Checkpoints

Long tasks should checkpoint after major stages. If the session is compacted or restarted, reload the checkpoint and approved artifacts rather than relying on memory.

## Safety

Push, merge, destructive Git, credential-sensitive, security-boundary, or production-impacting actions remain explicit human decisions unless the user has already approved that exact operation.

## Operational helpers

For long or highly governed work, these smaller workflow skills can be invoked directly:

- `agent-alignment` — align specialist roles before Gate A.
- `checkpoint-resume` — safely resume from durable state and reconcile SHA drift.
- `clean-validation` — prove reproducibility without destroying the active working tree.
- `project-traceability` — refresh REQ → DES → IMP → VAL/FND/RSK links.
- `test-oracle-design` — turn acceptance criteria into mechanical pass/fail evidence.
- `observability-evidence` — define/verify logs, metrics, traces, and budgets.

GitHub Copilot prompt launchers exist for each of these under `.github/prompts/`.

## Hard operating limits

- target less than 80% active model context;
- checkpoint and compact/start fresh before crossing it;
- run at most four substantial implementation iterations per session;
- one role owns repository mutation at a time;
- Git Manager is the sole commit writer.
