---
name: docs-code-alignment
description: Compare documentation with implementation and align stale claims to current evidence.
---

# Docs ↔ Code Alignment
Identify authoritative docs and implementing code/config/tests. Compare claim-by-claim. Classify aligned, docs stale, implementation diverged, ambiguous, or unknown. If current code is authoritative, update stale docs. If approved design is authoritative, escalate code divergence. Preserve evidence references.

## Extracting testable claims
For each claim in the docs, record: the claim text (a plain-English, verifiable statement — e.g. "the service exposes `POST /api/config`"); the claim type (API, data model, dependency, configuration, integration); the verification path (grep pattern, file to inspect, test case); and the responsible owner (`system-designer`, `implementation-designer`, or `implementer`).

Well-formed claim: specific, verifiable, owned. Poorly-formed claim (flag as informational, ask the owner to clarify rather than blocking the gate): vague ("X and Y are integrated"), unverifiable ("the system is fast"), or unowned ("something should work").

## Severity classification
| Severity | Definition | Action | Gate Impact |
|---|---|---|---|
| Critical | Contract mismatch (API signature changed, schema incompatible, endpoint removed) or an undocumented critical path, where the mismatch blocks downstream work or breaks an existing integration. | Owner must fix before the gate can pass. | Blocks. |
| Blocking | Docs promise a feature the code hasn't started or is still in draft, and the feature is needed for the gate. | Owner completes the code or updates the docs. | Blocks. |
| Minor | Docs describe old behavior but the code is correct and newer. | Owner updates docs next iteration; notify, don't block. | Does not block; log for backlog. |
| Informational | Code-quality note, pattern suggestion, or tech-debt pointer. | Log for backlog. | Does not block. |

## Convergence loop
Run the validator whenever discovery artifacts are refreshed, the implementer has produced or updated code, design/implementation docs change, or before a design-build gate. If BLOCKED: emit the report, route issues to owners (docs owner fixes docs, code owner fixes/completes code), re-run after fixes land, repeat until PASS or only minor/informational issues remain. Gate progression requires 0 critical and 0 blocking issues; minors are logged, not blocking.
