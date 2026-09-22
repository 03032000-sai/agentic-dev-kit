# GitHub Copilot Repository Instructions

Read `/AGENTS.md` as the canonical operating contract.

## Substantial-change behavior
For non-trivial features, fixes, refactors, and behavioral changes, use the `incremental-design-build` workflow rather than jumping directly to code.

The workflow requires:
- fresh Stage 0 repository context;
- Change Brief + mechanical Definition of Done;
- safe branch/checkpoint state;
- progressive disclosure;
- agent-alignment round;
- System Design + fresh Gate A critique;
- Implementation Design + fresh Gate B critique;
- bounded implementation iterations;
- deterministic local validation;
- clean-context validation when warranted;
- fresh Gate C critique;
- traceability and PR-ready Git handoff.

## Role isolation
Prefer custom agents in `.github/agents/` for specialist responsibilities. The agent that authors an artifact should not be its only reviewer.

## Evidence
Classify meaningful claims as `confirmed`, `documented`, `inferred`, or `unknown`. Deterministic tool output outranks model confidence. Missing validation remains missing.

## Safety
Do not perform destructive/history-rewriting Git actions, credential-sensitive actions, production-impacting operations, push, or merge without explicit approval.

If checkpoint/context integrity fails, stop mutation and switch to read-only planning until restored.
