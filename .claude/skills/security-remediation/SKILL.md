---
name: security-remediation
description: Triage and remediate security findings through evidence confirmation, least-privilege design, regression tests, deterministic rescanning, and independent review.
---

# Security Remediation

Capture exact finding/scanner scope, confirm/reproduce when possible, enrich reachability/exploitability without erasing scanner evidence, design the smallest fix, and require explicit review for auth/crypto/secrets/trust-boundary/production-permission changes.

Add regression evidence, rerun the originating scanner, verify discovery scope, then use a fresh Security Reviewer/critic for bypasses and fail-open behavior.

Zero expected packages/files/rules scanned is failure—not clean.
