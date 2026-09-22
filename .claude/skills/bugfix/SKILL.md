---
name: bugfix
description: Diagnose and fix a non-trivial defect using reproduction evidence, root-cause analysis, regression tests, design gates when needed, and independent closure review.
---

# Bug Fix

Establish expected vs actual behavior and reproducible evidence before editing. Perform focused discovery, identify a confirmed root cause (or explicitly label the hypothesis), decide whether the defect exposes a system-design gap, and route through Gate A/B when warranted.

Add or identify a regression oracle that demonstrates the original defect when feasible. Implement the smallest durable correction, run targeted then broader validation, use clean-context validation when risk warrants, and finish with a fresh Gate C critic.

Never suppress symptoms with broad fallbacks, weaken tests to pass, mix unrelated cleanup, or present correlation as confirmed root cause.
