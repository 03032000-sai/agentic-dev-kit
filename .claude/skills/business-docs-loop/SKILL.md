---
name: business-docs-loop
description: Turn a codebase into cited, plain-language business documentation for non-technical readers. Use when the deliverable is business-facing documentation, not code.
---

# Business Documentation Loop

Maintain a Change Brief scoped to documentation, not code changes.

1. Business Scope Intake confirms target repo/scope and scaffolds run state.
2. Codebase Cartographer builds the structural map with a stable ID registry.
3. Domain Glossary Curator builds the term glossary (gate: no later stage introduces an undefined term).
4. Business Rule Miner extracts cited decision tables; WHAT is `confirmed`, WHY is `inferred`.
5. Process Capability Mapper reconstructs capability swimlane flows, citing every step.
6. Fresh critic reviews the map, glossary, rules, and capabilities for code-anchored evidence before any narrative is written; close BLOCKING findings.
7. Business Doc Writer produces plain-language narrative from approved findings only — no code access, zero new claims.
8. Fresh critic reviews the narrative as a stand-in for a non-technical reader: readability, jargon, trust; close BLOCKING findings.
9. Business Doc Publisher compiles the traceability matrix, gap register, and coverage report.

Every claim carries its evidence class (`confirmed|documented|inferred|unknown`) and source citation through to publication.
