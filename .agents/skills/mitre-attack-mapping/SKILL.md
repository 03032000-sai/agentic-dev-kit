---
name: mitre-attack-mapping
description: Deterministically map security finding categories to MITRE ATT&CK techniques for coverage reporting without model free-association.
---

# MITRE ATT&CK Mapping

## Principle
ATT&CK mapping is a coverage/reporting layer, not proof that an adversary executed a technique.

## Deterministic mapping
Use a versioned static mapping table from finding category/CWE/rule family to candidate ATT&CK technique IDs. The table should be reviewed and stored with the project.

Do not ask a model to invent technique IDs from prose.

## Mapping record
Capture:
- finding/rule ID;
- CWE/category;
- mapped ATT&CK technique ID/name;
- mapping-table version/source;
- confidence rule;
- status: mapped | unmapped.

If no reviewed mapping exists, leave the finding unmapped.

## Coverage
Compare pre-remediation and post-remediation technique coverage for reporting. Do not imply that closing one finding eliminates the entire ATT&CK technique from the system.
