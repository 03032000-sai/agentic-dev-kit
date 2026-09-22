---
name: mitre-attack-mapping
description: Deterministically map enriched security findings to MITRE ATT&CK techniques for coverage reporting.
---

# MITRE ATT&CK Mapping
Map each enriched finding to a MITRE ATT&CK technique using a static, deterministic pattern table (finding category/CWE → technique ID) — never let a model free-associate a technique ID. Track pre-fix and post-fix technique coverage to show remediation impact. Leave a finding unmapped rather than forcing a low-confidence match.
