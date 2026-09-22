---
name: bugfix
description: Diagnose and fix a non-trivial bug while preserving unrelated behavior. Use when current behavior is incorrect or regressed.
---

# Bug Fix
1. Reproduce or establish failure evidence.
2. Record expected vs actual behavior.
3. Identify smallest responsible boundary.
4. Decide whether design is impacted.
5. Run design gates if needed.
6. Add regression test when feasible.
7. Implement smallest safe correction.
8. Run local validation and clean validation when risk warrants.
9. Critic checks regression scope and hidden behavior changes.
10. Update docs if contracts/behavior changed.
Do not weaken tests or suppress errors to make the bug disappear.
