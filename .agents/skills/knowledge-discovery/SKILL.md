---
name: knowledge-discovery
description: Answer repository architecture, behavior, and domain questions through evidence-first discovery, stable claims, and fresh-context critique without modifying product code.
---

# Knowledge Discovery

## Goal
Produce a trustworthy answer to a repository/system question without turning analysis into unverified narrative.

## Flow
1. Restate the exact question and scope.
2. Bootstrap current repo/branch/SHA context if missing.
3. Break the question into answerable sub-questions.
4. Discover candidate evidence using progressive disclosure.
5. Build a claim/evidence map.
6. Separate WHAT from WHY:
   - WHAT may be confirmed by executable evidence;
   - WHY requires authoritative documentation or remains inferred/unknown.
7. Synthesize the minimum model that answers the question.
8. Hand the map/findings to a fresh Map or Findings Critic.
9. Publish confirmed facts, documented claims, inferences, and unresolved gaps separately.

## Evidence hierarchy
Prefer direct code/config/test/runtime evidence for current behavior, then authoritative design/docs, then inference. Do not let stale prose override executable current state without noting the conflict.

## Output
- question/scope;
- concise answer;
- evidence-backed architecture/flow when useful;
- claim/evidence table;
- unknowns/conflicts;
- source SHA;
- critic findings.

## Prohibitions
No product mutation, no invented historical intent, no pretending incomplete search proves absence.
