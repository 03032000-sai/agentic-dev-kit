---
name: implementation-design
description: Convert approved system design into a Gate B-ready repository-specific technical plan.
---

# Implementation Design

Map the approved system design to:
- exact files/modules;
- functions/classes/symbols;
- API/schema/event/config changes;
- persistence/state;
- dependencies;
- error/retry contracts;
- compatibility/migration;
- unit/integration/E2E/negative tests;
- telemetry/logging/metrics/tracing;
- rollout/deployment;
- rollback/recovery;
- exact validation commands;
- ordered implementation slices;
- requirement traceability.

If a missing architectural decision is discovered, reopen system design rather than hiding it in the technical plan. Do not implement while using this skill.
