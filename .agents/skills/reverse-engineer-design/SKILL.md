---
name: reverse-engineer-design
description: Reconstruct current system design and implementation design from executable evidence while marking inference and refusing invented rationale.
---

# Reverse Engineer Design

## Phase 1 — Abstract current system
Derive:
- system boundaries and actors;
- component responsibilities;
- contracts/interfaces;
- invariants;
- state/data/control flows;
- failure/recovery behavior;
- security/reliability/observability signals.

## Phase 2 — Concrete implementation
Map the abstract design to:
- repositories/files/modules;
- entry points;
- classes/functions;
- APIs/events/schemas;
- persistence/state;
- external integrations;
- tests;
- CI/CD/deployment topology where evidenced.

## Evidence classes
Every material statement is confirmed, documented, inferred, or unknown.

## Rationale rule
Implementation structure may show WHAT exists; it rarely proves WHY it was chosen. Do not manufacture historical intent.

## Review
Use a fresh Map Critic for structural completeness and a Findings Critic for unsupported claims.

## Output
Current-state system-design artifact, implementation-design artifact, source SHA, evidence links, unknowns, and drift notes.
