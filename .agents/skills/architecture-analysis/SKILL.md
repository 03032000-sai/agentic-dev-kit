---
name: architecture-analysis
description: Analyze existing architecture boundaries, contracts, flows, state, failure modes, and cross-cutting concerns from repository evidence.
---

# Architecture Analysis

## Questions
Use when the user needs to understand how the current system is structured or where an architectural concern lives.

Analyze:
- system/context boundaries;
- components and ownership;
- synchronous/asynchronous contracts;
- data/state ownership;
- request/event flows;
- failure/retry paths;
- trust/security boundaries;
- scaling/reliability patterns;
- observability;
- deployment topology;
- architectural hotspots/coupling.

## Evidence
Ground each architectural edge in code/config/schema/test/deployment evidence and mark inferred relationships.

## Diagrams
Use Mermaid context/component/sequence/state diagrams when they make boundaries or behavior easier to inspect.

## Output
Current-state architecture model, evidence links, risks/coupling, unknowns, and source SHA. Do not turn analysis into redesign unless requested.
