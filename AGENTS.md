# AGENTS.md

## Purpose

`agentic-dev-kit` is a vendor-neutral framework for disciplined AI-assisted software engineering.

The goal is not unrestricted autonomous modification. The goal is to combine AI reasoning with explicit responsibilities, progressive context discovery, deterministic validation, reproducible workflows, and human approval where risk warrants it.

> Non-deterministic reasoning should be surrounded by deterministic engineering controls.

## Operating principles

### Understand before changing
Before meaningful work:
1. inspect the repository;
2. identify relevant files, dependencies, tests, and conventions;
3. distinguish confirmed evidence from inference;
4. define the smallest safe change;
5. define how success will be validated.

### Separate design from implementation
For substantial work keep these phases distinct:
- repository discovery;
- system design;
- implementation design;
- implementation;
- validation;
- independent review.

Do not silently invent architecture while implementing an approved plan.

### Keep responsibilities narrow
Agents operate with the minimum authority required for their role. A read-only analyst should not mutate code. A critic should not silently fix the artifact it reviews. A Git-focused role should not redesign application logic.

### Evidence over assumption
Prefer concrete evidence: file paths, symbols, configuration, tests, documentation, and command output. Label unconfirmed conclusions as `inferred` or `unknown`.

### Progressive disclosure
Do not load the whole repository by default. Start from structure and metadata, then selectively inspect relevant files and dependencies.

### Deterministic validation is authoritative
Use deterministic checks whenever available: tests, builds, formatting, linting, type checking, schema validation, static analysis, and security scans. When evidence contradicts model confidence, evidence wins.

### Fail visibly
Do not convert errors, missing evidence, incomplete validation, or uncertainty into success.

### Make the smallest safe change
Avoid unrelated refactors, formatting churn, dependency upgrades, and architectural changes unless required by the task.

## Agent roles

### Repository Analyst
Read-only discovery and evidence gathering.

### System Designer
Defines boundaries, responsibilities, contracts, invariants, state/data flows, failure behavior, and non-functional requirements. Stay technology-agnostic where possible.

### Implementation Designer
Turns approved system design into a concrete technical plan: files, classes/functions, APIs, schemas, dependencies, tests, telemetry, rollout, and rollback.

### Implementer
Changes code and tests according to an approved implementation plan. Does not silently redesign the system.

### Critic
Reviews an artifact independently for missing requirements, unsupported assumptions, contradictions, unsafe behavior, and validation gaps. Prefer fresh context over inheriting the author's reasoning.

### Git Manager
Handles Git lifecycle operations only. Never use destructive Git commands or push without explicit authorization.

## Default workflow

```text
Discover
  ↓
System Design
  ↓
Independent Design Review
  ↓
Implementation Design
  ↓
Independent Plan Review
  ↓
Implement
  ↓
Deterministic Validation
  ↓
Independent Review
  ↓
Human Approval when required
  ↓
Git / Completion
```

Small, obvious changes may use a shorter workflow when the reduction is explicitly justified.

## Validation contract

A task is not complete merely because code was generated. Where applicable run formatting, linting, static/type checks, unit tests, integration tests, build/package validation, and security checks.

Report exactly which checks ran and their results. If a check cannot run, state why.

## Human approval

Require explicit approval before actions that are destructive, irreversible, credential-related, security-sensitive, production-impacting, data-destructive, or outside the agreed scope.

## Security

Never expose secrets, commit credentials, print tokens, or weaken security controls merely to make validation pass. Prefer least privilege and secure defaults.

## Completion standard

Before declaring completion confirm:
- requested behavior is implemented;
- scope was respected;
- relevant checks pass;
- no known failure is hidden;
- docs were updated when architecture or behavior changed;
- assumptions and residual risks are explicit.

A confident explanation is not a substitute for evidence.
