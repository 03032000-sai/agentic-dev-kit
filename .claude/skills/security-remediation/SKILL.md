---
name: security-remediation
description: Triage, design, implement, and verify security remediation using deterministic evidence, least privilege, and explicit human review boundaries.
---

# Security Remediation

Use for SAST/SCA findings, vulnerable dependencies, unsafe permissions, auth defects, secret exposure, or risky agent/tool behavior.

## Flow
1. Establish the finding source and exact affected component.
2. Reproduce/confirm with deterministic evidence where possible.
3. Determine reachability/exploitability without overstating certainty.
4. Build a remediation Change Brief and non-goals.
5. Design the smallest durable fix.
6. Require explicit review for changes to authn/authz, cryptography, secrets, trust boundaries, or production permissions.
7. Implement with regression tests.
8. Re-run the originating scanner/check plus relevant tests.
9. Run fresh Security Reviewer/Implementation Critic.
10. Record residual risk and evidence.

## Evidence rules
- Scanner output is authoritative only for what was actually scanned.
- Zero expected packages/rules/files scanned is a validation failure, not "clean."
- Severity is not the same as exploitability.
- Missing enrichment never erases a scanner finding.
- A dependency manifest edit is not proof until the resolved graph changes.

## Autofix boundary
Mechanical Tier-1 fixes may be automated only when semantics are narrow, deterministic, covered by positive/negative fixtures, and do not alter auth, authorization, crypto, or secret handling.

## Completion
A finding is closed only when the vulnerable behavior/dependency is no longer present in deterministic evidence and regression coverage exists where feasible.
