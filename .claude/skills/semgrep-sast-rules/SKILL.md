---
name: semgrep-sast-rules
description: Author and extend Semgrep SAST rules with safe, reviewable autofix templates.
---

# Semgrep SAST Rules
Write Semgrep rules scoped to a specific vulnerability pattern with a precise `message`, `severity`, and language-appropriate `metadata` (CWE/OWASP mapping). Prefer narrow `pattern`/`pattern-either` matches over broad regex to minimize false positives. For Tier-1 findings (unambiguous, mechanical fixes), pair the rule with an autofix template and require a passing test fixture (true positive + true negative) before enabling it in CI. Never auto-apply a fix that changes authentication, authorization, or cryptographic behavior without human review.
