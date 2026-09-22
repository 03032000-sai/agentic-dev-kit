---
name: transitive-dependency-remediation
description: Remediate CVEs in transitive (indirect) dependencies that cannot be fixed by simple manifest version edits, across Maven, npm, and pip. Use when injecting Maven dependencyManagement overrides, adding npm overrides/resolutions, pinning pip transitive packages, or discovering manifests across a monorepo.
---

# Transitive Dependency Remediation

## Overview
When an SCA scan reports a CVE in a transitive dependency, a direct version-string edit in the manifest is not enough. Ecosystem-specific overrides are required:
- **Maven** (`pom.xml`): inject `<dependencyManagement>` version overrides.
- **npm** (`package.json`): add `"overrides"` (npm ≥ 8.3) and `"resolutions"` (yarn).
- **pip** (`requirements.txt`): pin transitive packages not already declared.

Distinguish direct vs. transitive by parsing declared dependencies (Maven: `<dependencies>`, `<parent>`, plugins; npm: `package.json`), so only genuinely indirect dependencies get over-pinned.

Manifests are located recursively, excluding cache/build directories (`node_modules`, `target`, `build`, `dist`, `vendor`, `.venv`, `bin`, `obj`, …).

## When to Use This Skill
- An SCA CVE lands in an indirect dependency (no direct manifest line to bump).
- You need a Maven `<dependencyManagement>` override or npm `overrides`/`resolutions`.
- You need to pin a transitive pip package.
- You need to enumerate all manifests in a monorepo/multi-module tree.

## Do NOT apply this skill when
- The CVE is in a direct dependency (bump the declared version normally).
- Running/parsing the scan itself (use `trivy-sca-scanning`).
- Patching a downloaded/generated manifest under an excluded directory — never edit `node_modules`, `target`, etc.

## Workflow
1. Discover manifests → group by ecosystem.
2. Classify the CVE's package as direct vs. transitive for that manifest.
3. Apply the ecosystem-specific override.
4. Re-run the SCA scan to confirm the CVE is resolved and no new breakage appears.

## Example
```xml
<!-- Maven transitive override -->
<dependencyManagement>
  <dependencies>
    <dependency>
      <groupId>com.fasterxml.jackson.core</groupId>
      <artifactId>jackson-databind</artifactId>
      <version>2.17.1</version>
    </dependency>
  </dependencies>
</dependencyManagement>
```
