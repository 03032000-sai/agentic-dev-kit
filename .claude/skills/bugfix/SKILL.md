---
name: bugfix
description: Diagnose and fix a non-trivial defect using reproduction evidence, root-cause analysis, regression tests, design gates when needed, and independent closure review.
---

# Bug Fix

## Goal
Correct the root cause while preserving unrelated behavior.

## Flow
1. **Establish failure evidence.** Capture expected vs actual behavior, environment, repro steps, logs/tests, and affected scope.
2. **Focused discovery.** Trace the failing path, state, dependencies, recent relevant changes, and nearby tests.
3. **Root-cause hypothesis.** Distinguish confirmed cause from plausible correlation.
4. **Design-impact decision.**
   - local implementation defect → implementation plan may be sufficient;
   - contract/invariant/boundary failure → reopen System Design / Gate A.
5. **Regression oracle.** Add or identify a test/check that demonstrates the bug when feasible.
6. **Implementation design / Gate B** for non-trivial fixes.
7. **Implement smallest durable correction.**
8. **Targeted local validation**, then broader regression checks.
9. **Clean-context validation** when release risk warrants.
10. **Fresh Gate C critic** reviews root-cause closure, regression risk, diff, and evidence.
11. Update docs if externally visible behavior/contracts changed.

## Anti-patterns
Do not:
- suppress the symptom with a broad catch/fallback;
- weaken/delete a failing test;
- claim a root cause solely from temporal correlation;
- fix unrelated cleanup in the same change;
- skip negative/failure-path testing when the bug occurred there.

## Completion evidence
The original repro no longer fails, the regression oracle passes, required broader checks pass, and the critic finds no unresolved blocking regression/scope issue.
