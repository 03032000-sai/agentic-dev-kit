---
name: business-docs-loop
description: Convert implementation evidence into cited plain-language business documentation using map, glossary, findings, fidelity, and code-blind review gates.
---

# Business Documentation Loop

## Invariants
- code/config/tests establish WHAT;
- WHY requires authoritative documentation or remains inferred/unknown;
- every material claim carries evidence;
- narrative writers introduce zero new facts;
- specialist critics use fresh context;
- publication records source SHA(s).

## Flow
1. Business Scope Intake defines audience/questions/scope/non-goals.
2. Codebase Cartographer creates stable IDs and evidence-backed map.
3. Fresh Map Critic reviews coverage.
4. Domain Glossary Curator establishes `TERM-###` vocabulary; glossary gate blocks unexplained domain terms.
5. Business Rule Miner extracts `RULE-###` decision tables with WHAT/WHY separation.
6. Fresh Findings Critic verifies evidence classes/citations.
7. Process Capability Mapper creates `CAP-###` / `PROC-###` flows and swimlanes.
8. Business Doc Writer receives approved findings only and writes plain-language narrative with zero new factual claims.
9. Fidelity critic verifies narrative → approved finding/evidence.
10. Code-blind reader checks readability, jargon, unexplained identifiers, and trust.
11. Publisher emits narrative, diagrams, glossary, traceability matrix, gap register, coverage report, and source SHA(s).

## Stable IDs
Use CMP, ENT, STORE, INT, JOB, RULE, CAP, PROC, TERM namespaces.

## Gate behavior
Blocking evidence gaps return to the producing stage. Do not paper over unknown business intent.
