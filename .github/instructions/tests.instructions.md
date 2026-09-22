---
applyTo: "**/tests/**,**/*test*,**/*spec*"
---

# Test Instructions

Tests are deterministic evidence, not implementation decoration.

- map tests to requirements, risks, contracts, or regressions;
- prefer behavior assertions over private implementation trivia;
- bug fixes should include a regression oracle when feasible;
- refactors should preserve characterization coverage;
- include negative/failure paths when meaningful;
- cover authorization/security boundaries where relevant;
- do not delete, weaken, skip, or broad-catch tests merely to make a change pass;
- keep fixtures deterministic and minimal;
- a test that was not executed is planned evidence, not passing evidence;
- zero discovered tests when tests are expected is suspicious and must be surfaced.
