---
applyTo: "**/test_*.py,**/*_test.py,**/tests/**"
---

For tests:
- assert meaningful behavior rather than implementation trivia;
- include failure paths and boundary cases where risk warrants;
- keep fixtures minimal and deterministic;
- control network/time/random dependencies;
- make regression tests explain the behavior they protect.
