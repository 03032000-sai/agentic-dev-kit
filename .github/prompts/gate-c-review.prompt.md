---
description: Run a fresh-context Gate C critique of the candidate diff and deterministic validation evidence.
agent: implementation-critic
---

Read `AGENTS.md`.

Pin the candidate SHA and review Change Brief/DoD, approved Gate A/B artifacts, actual diff, local/clean validation, documentation, prior findings, and residual risks.

Look for missing requirements, scope/design drift, hidden breakage, weak regression coverage, security regressions, stale docs, wrong-SHA evidence, and misleading completion claims.

Return BLOCKING / IMPORTANT / ADVISORY findings plus PASS/FAIL Gate C recommendation. Do not silently fix the reviewed implementation.
