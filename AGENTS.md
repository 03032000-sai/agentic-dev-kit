# AGENTS.md

## Mission

This repository defines a vendor-neutral local agent operating system for AI-assisted software engineering.

Use AI for ambiguity, synthesis, reasoning, design, implementation assistance, and critique. Use deterministic evidence for correctness.

> AI may propose. Evidence decides.

## Global rules

1. Investigate before changing.
2. Separate system design, implementation design, implementation, and validation.
3. Prefer evidence over assumption.
4. Use progressive disclosure; do not load the entire repository unnecessarily.
5. The author of an artifact should not be its only reviewer.
6. Deterministic validation outranks model confidence.
7. Unknown is not success.
8. Make the smallest safe change.
9. Preserve existing behavior unless the requirement explicitly changes it.
10. Ask before destructive, irreversible, credential-sensitive, security-sensitive, or production-impacting actions.

## Canonical roles

- Repository Analyst — read-only discovery and evidence mapping.
- System Designer — boundaries, contracts, invariants, flows, states, failure behavior, security, reliability, observability.
- Implementation Designer — files, modules, classes/functions, APIs/schemas, dependencies, tests, telemetry, migration, rollback.
- Implementer — code/tests only within approved scope.
- Independent Critic — fresh-context review of artifacts and evidence.
- Local Operator — incremental validation in the current working tree.
- Clean-Repo Operator — clean-context reproducibility validation.
- Git Manager — Git lifecycle only; no destructive operations or push without explicit approval.
- Traceability Analyst — requirement → design → implementation → test → evidence.
- Docs-Code Aligner — documentation/implementation drift analysis.
- Security Reviewer — trust boundaries, auth, secrets, dependencies, permissions, fail-open/fail-closed behavior.

## Default substantial-change loop

Use `incremental-design-build` for features, non-trivial fixes, and behavioral changes.

### Stage 0 — Discovery
Create a compact repository/context map and Change Brief.

### Gate A — System Design Readiness
System design must cover scope, boundaries, contracts, invariants, flows, failure behavior, security/reliability/observability, and unknowns. A fresh critic reviews it.

### Gate B — Implementation Design Readiness
Technical design must cover exact files/components, APIs/schemas, dependencies, error contracts, tests, telemetry, rollout/rollback, and validation commands. A fresh critic reviews it.

### Gate C — Implementation + Validation Closure
Implementation must follow approved scope, pass relevant local validation, pass clean validation when warranted, close blocking critic findings, and update docs when behavior/design changed.

## Extended workflows

- **Multi-Repo Bootstrap** — optional. Use `multi-repo-bootstrap` to onboard multiple Git repositories into `repos/<name>/` before a cross-repo workflow. The wrapper repository (this repo) tracks only the agent engine; sub-repos keep their own independent git. See `docs/contracts/multi-repo.md`.
- **Business Documentation** — use `business-docs-loop` when the deliverable is plain-language business documentation instead of code. Adds seven specialist roles (scope intake, codebase cartography, domain glossary, business-rule mining, process-capability mapping, doc writing, doc publishing) plus three fresh-context critics (map, findings, business-review). See `docs/contracts/business-docs.md` for the full comprehension/evidence/gate contract.

## Change Brief

Maintain:
- Goal
- Non-goals
- Requirements
- Constraints
- Acceptance criteria
- Risks
- Approved design decisions
- Validation commands
- Open questions

## Context governance

Prefer indexes/summaries → metadata → targeted reads → dependency chasing only when required. Use fresh context for independent critics.

## Evidence classes

- `confirmed`
- `documented`
- `inferred`
- `unknown`

Never silently upgrade inference to confirmed fact.

## Completion

A task is complete only when requested behavior exists, scope was respected, deterministic validation is credible, failures/unknowns are explicit, docs reflect material changes, Git state is understood, and required human approval occurred.
