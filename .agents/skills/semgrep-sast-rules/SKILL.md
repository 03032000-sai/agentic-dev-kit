---
name: semgrep-sast-rules
description: Author, test, tune, and operationalize precise Semgrep SAST rules with controlled autofix boundaries.
---

# Semgrep SAST Rules

## Goal
Create narrow, reviewable static-analysis rules that detect a specific code pattern with acceptable false-positive/false-negative behavior.

## Rule design
Each rule should define:
- stable rule ID;
- languages;
- severity;
- precise message;
- CWE and/or OWASP metadata where applicable;
- references/rationale;
- focused `pattern`, `pattern-either`, metavariable constraints, or taint mode;
- optional safe autofix only for mechanical transformations.

Prefer semantic patterns over broad regex.

## Test fixture
Every custom rule should have:
- at least one true-positive fixture;
- at least one true-negative fixture;
- expected finding count/location;
- autofix expectation if enabled.

For data-flow bugs, consider a companion taint rule rather than stretching a simple pattern beyond reliability.

## Autofix tiers
**Tier 1 — mechanical:** may be proposed automatically after fixtures pass.
**Tier 2 — semantic:** generate guidance/patch for human review.
**Tier 3 — security-boundary:** never auto-apply changes to authn/authz, crypto, trust boundaries, or secret handling.

## CI behavior
Fail or warn according to repository policy, but never report "no findings" when the rule pack failed to load or target files were not scanned.

## Verification
After remediation, run the exact rule against the changed code and its fixtures; preserve the result in validation evidence.
