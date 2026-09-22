---
name: security-remediation
description: Triage and remediate security findings through evidence confirmation, least-privilege design, regression tests, deterministic rescanning, and independent review.
---

# Security Remediation

## Stage 1 — Finding intake
Capture source/tool, rule/CVE, affected component/version/path, severity, scanner scope, and raw evidence reference.

## Stage 2 — Confirm and enrich
Determine:
- whether the finding is reproducible;
- reachability/exposure where evidence permits;
- KEV/EPSS/advisory context when available;
- current compensating controls;
- fixed version/remediation options.

Do not downgrade a finding merely because enrichment is missing.

## Stage 3 — Remediation design
Choose the smallest durable fix. Changes to authn/authz, cryptography, secrets, trust boundaries, or production permissions require explicit human review.

## Stage 4 — Implement + regression
Add a regression oracle where feasible. For dependency fixes, verify the resolved graph; for code findings, rerun the exact rule/fixture.

## Stage 5 — Deterministic verification
Re-run the originating scanner and relevant tests. Verify discovery scope is still correct. Zero expected packages/files/rules scanned is a failure, not "clean."

## Stage 6 — Fresh security critique
Review bypasses, fail-open behavior, new attack surface, privilege expansion, and misleading closure claims.

## Completion
Close only when the original vulnerable behavior/dependency is absent from credible evidence, validation passes, and residual risk is explicit.
