---
applyTo: "**/*.py,**/pyproject.toml,**/uv.lock,**/requirements*.txt"
---

# Python Instructions

Follow the repository's established Python tooling first.

- prefer typed, explicit interfaces for important contracts;
- keep dependency intent in the authoritative project manifest;
- when uv is established/approved, use pyproject + lockfile and validate from a fresh environment;
- do not churn package tooling during unrelated changes;
- avoid broad exception handling that hides security/configuration failures;
- keep I/O and side effects testable;
- add deterministic unit/integration coverage for behavior changes;
- do not expose credentials in config, logs, fixtures, or command examples;
- respect the approved implementation design rather than introducing framework changes opportunistically.
