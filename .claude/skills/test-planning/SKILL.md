---
name: test-planning
description: Create a risk-based deterministic validation plan. Use for unit, integration, end-to-end, regression, failure-path, or operational validation. Do not use as a substitute for actually running available tests.
---

# Test Planning
1. Map each requirement to validation.
2. Identify happy paths, boundaries, failures, regressions, security-sensitive paths, and state/concurrency risks.
3. Choose the smallest effective layer: unit, integration, contract, end-to-end, static analysis, build/package, or security scan.
4. Define exact commands when available.
5. Distinguish tests that exist from tests that must be added.
6. Define pass/fail criteria.
7. Report validation that cannot be performed and why.

A planned test is not evidence that the change passes.
