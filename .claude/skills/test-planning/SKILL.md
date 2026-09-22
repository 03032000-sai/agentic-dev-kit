---
name: test-planning
description: Translate requirements and risks into deterministic validation evidence across unit, integration, E2E, negative, build, and security checks.
---

# Test Planning

For each requirement/risk identify:
- behavior under test;
- test level;
- fixture/setup;
- expected result;
- failure-path result;
- command;
- environment;
- evidence artifact.

Cover:
- happy path;
- boundaries;
- invalid input;
- failure/retry;
- concurrency/idempotency where relevant;
- compatibility/regression;
- authorization/security;
- observability;
- migration/rollback when relevant.

Distinguish existing tests from tests that must be added. A planned test is not passing evidence.
