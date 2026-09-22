---
description: Diagnose and fix a non-trivial bug with root-cause evidence, regression coverage, and governed design/validation.
---

Read `AGENTS.md` and invoke the `bugfix` skill.

Do not edit first. Start with a failure packet: expected vs actual behavior, reproduction evidence, environment, affected scope, and known impact. Perform focused discovery, distinguish symptom from confirmed root cause, and decide whether the fix requires Gate A and/or Gate B.

Require a regression oracle when feasible. Implement the smallest durable correction, run targeted and broader deterministic validation, use clean-context validation when warranted, and finish with a fresh Gate C critic.

At pauses report root-cause confidence, current gate/stage, evidence, open risks, and next role.
