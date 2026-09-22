---
name: observability-evidence
description: Define and verify logs, metrics, traces, dashboards, and measurable service budgets as evidence for production readiness and post-deploy validation.
---

# Observability Evidence

## Design
For material behavior identify:
- success signal;
- failure signal;
- latency/throughput/error indicators;
- correlation/request/trace identifiers;
- retry/backoff visibility;
- dependency health;
- security/audit events where required;
- alert/dashboard ownership.

## Quality rules
- logs must not expose secrets or sensitive payloads;
- metrics need stable labels with bounded cardinality;
- traces must cross important boundaries where feasible;
- alerts should map to actionable failure conditions;
- "we log errors" is not an observability plan.

## Verification
Use deterministic evidence where possible:
- expected log event;
- metric increment/value;
- trace/span presence;
- alert condition test;
- dashboard query;
- latency/error budget comparison.

## Closure
Gate C/release readiness should distinguish observability that is implemented from observability merely planned.
