---
description: Run deterministic incremental validation in the current working tree and capture exact evidence.
agent: local-operator
---

Read `AGENTS.md` and the current validation plan.

Run the smallest sufficient validation ladder: format/syntax, lint/static/type checks, targeted/broad tests, build/package, security/dependency scans, and smoke checks as warranted.

Capture command, working directory, exit result, discovery counts where relevant, concise result, and artifact/log references. Failure remains failure; zero expected discovery is suspicious. Do not redesign product behavior.
