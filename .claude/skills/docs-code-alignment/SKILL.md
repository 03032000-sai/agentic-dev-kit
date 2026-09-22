---
name: docs-code-alignment
description: Compare material documentation claims with executable behavior and approved design, classify drift, and correct only evidence-backed mismatches.
---

# Docs ↔ Code Alignment

## Goal
Determine whether documentation describes current behavior, target behavior, or stale intent—and align it without inventing history.

## Flow
1. Select authoritative docs in scope.
2. Extract material claims.
3. Identify corresponding code/config/tests/design evidence.
4. Classify each claim:
   - aligned;
   - docs stale;
   - implementation diverged from approved target design;
   - ambiguous;
   - unknown.
5. Decide correction direction from source-of-truth policy.
6. Update only evidence-backed claims when authorized.
7. Run a fresh Findings Critic over corrected docs.

## Source-of-truth policy
- current-state behavior: executable code/config/tests normally dominate stale prose;
- future/target behavior: explicitly approved design may dominate current implementation;
- historical rationale: requires an authoritative source and is never reconstructed from code style alone.

## Output
Claim/drift table, corrected documents or proposed changes, unresolved ambiguities, source SHA, and validation links.

## Prohibitions
Do not make code and docs "match" by silently changing whichever is easier. Surface real design divergence.
