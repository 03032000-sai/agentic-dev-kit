---
name: safe-refactor
description: Improve internal structure while preserving externally observable behavior through characterization evidence, bounded steps, and independent regression review.
---

# Safe Refactor

## Goal
Change structure, not behavior.

## Before editing
1. Define the behavior contract that must remain unchanged.
2. Identify public APIs, schemas, side effects, timing/order constraints, persistence behavior, and performance-sensitive paths.
3. Locate characterization/regression tests.
4. Add missing characterization tests where feasible.
5. Create a narrow refactor plan and explicit non-goals.

## Execution
Refactor in small steps:
- one structural change at a time;
- run targeted validation after each meaningful step;
- preserve interfaces unless the Change Brief explicitly authorizes a change;
- avoid mixing feature/bug behavior into the refactor;
- checkpoint after substantial slices.

## Review
A fresh critic compares:
- before/after behavior contract;
- public interfaces;
- side effects;
- error behavior;
- tests;
- diff scope;
- performance-sensitive paths.

## Anti-patterns
Do not:
- "clean up" unrelated code;
- rename public interfaces without authorization;
- delete tests because implementation changed;
- hide behavior changes inside a refactor commit;
- claim equivalence solely because unit tests pass.

## Completion
Relevant characterization/regression checks pass, no unauthorized behavior change is detected, docs reflect only necessary structural changes, and Gate C has no blocking findings.
