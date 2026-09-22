---
name: transitive-dependency-remediation
description: Remediate vulnerable transitive (indirect) dependencies with ecosystem-specific override mechanisms.
---

# Transitive Dependency Remediation
Prefer an ecosystem's native override mechanism over forking or vendoring: Maven `dependencyManagement`, npm `overrides`/`resolutions`, pip constraint pins. Pin to the lowest version that resolves the CVE, not the latest, to minimize collateral change. Verify the override actually took effect (resolved dependency tree, not just the manifest) and re-run the SCA scan to confirm.
