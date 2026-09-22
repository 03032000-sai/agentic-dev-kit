---
applyTo: "**/*.py"
---

For Python changes:
- prefer explicit types at public boundaries;
- preserve repository conventions before adding new tooling;
- keep side effects visible;
- handle errors intentionally rather than with broad catch-all exceptions;
- update tests with behavior changes;
- avoid new dependencies when the existing stack or standard library is sufficient.
