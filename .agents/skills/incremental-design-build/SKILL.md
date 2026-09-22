---
name: incremental-design-build
description: Run the full governed design-build loop for a substantial feature, bug fix, or behavioral change. Use when discovery, design, implementation, validation, and independent critique are needed. Do not use for trivial edits.
---

# Incremental Design / Build

Maintain a Change Brief.

1. Stage 0: Repository Analyst produces task-focused evidence.
2. System Designer creates abstract design.
3. Gate A: fresh critic reviews; close BLOCKING findings.
4. Implementation Designer creates concrete technical plan.
5. Gate B: fresh critic reviews; close BLOCKING findings.
6. Implementer applies only approved scope.
7. Local Operator runs deterministic validation.
8. Clean-Repo Operator validates reproducibility when warranted.
9. Gate C: fresh critic reviews requirements, design, diff, validation, and docs.
10. Git Manager prepares completion. Require human approval where risk policy says so.
