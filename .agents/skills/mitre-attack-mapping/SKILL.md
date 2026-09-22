---
name: mitre-attack-mapping
description: Map enriched scan findings to MITRE frameworks deterministically (ATT&CK; extendable toward CWE→CAPEC→ATT&CK→D3FEND) and compute the pre/post-fix technique-coverage delta. Use when editing MITRE mapping tables, adding technique patterns, or reasoning about the deterministic no-LLM mapping contract.
---

# MITRE ATT&CK Mapping

## Overview
MITRE mapping runs at two barriers in the remediation workflow — pre-fix and post-fix — so the difference quantifies real risk reduction. The mapping is deterministic: a static keyword/pattern table plus KEV/EPSS exploitation signals. No LLM, no network on the mapping path, so results are reproducible and auditable.

Key operations: map enriched findings to ATT&CK techniques for a given phase (`pre_fix` | `post_fix`), writing a JSON + Markdown report; compute the post-fix delta (techniques present pre-fix, absent post-fix).

Mapping rules live in a pattern table (regex → technique_id/name/tactic) matched case-insensitively against each finding's component, title, summary, and CVE id. Unmatched findings are counted `unmapped`, never force-fitted.

## The Framework Chain (Mapping Model)
CWE (weakness) → CAPEC (attack pattern) → ATT&CK (technique) → D3FEND (countermeasure). ATT&CK is the implemented layer; when extending toward the full chain, keep every ID sourced from static tables (never LLM-generated) and label missing links `unmapped`.

## When to Use This Skill
- Adding/adjusting a pattern-rule entry (new weakness → technique mapping).
- Tuning the KEV/EPSS exploitation-signal boosts.
- Extending output toward CWE/CAPEC/D3FEND fields with explicit `unmapped` handling.
- Reasoning about the pre/post-fix delta artifacts.

## Do NOT apply this skill when
- The change would let a MITRE tag alter a pass/fail gate result — mapping enriches and prioritizes only; it never changes pass/fail.
- You would introduce an LLM or live network call into the mapping path (forbidden).
- Editing enrichment sources (use `vuln-enrichment-prioritization`).

## Workflow
1. Locate the pattern-rule table / classification function in the mapping tool.
2. Add the regex→technique entry using a real MITRE ATT&CK Enterprise technique ID.
3. Keep unmatched findings explicit (`unmapped`) — do not broaden a pattern to force a match.
4. Verify the same finding + same tables → identical output across runs (determinism).
5. Confirm the mapping step still writes both the JSON and Markdown artifacts.

## Example
```python
# Pattern-rule entry
(r"ldap[-_ ]?inject", "T1190", "Exploit Public-Facing Application", "Initial Access"),
```
