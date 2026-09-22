---
name: trivy-sca-scanning
description: Run and interpret Trivy dependency, filesystem, image, or IaC scans with explicit discovery checks and fail-closed evidence.
---

# Trivy SCA Scanning

## Discovery first
Identify the authoritative target:
- lockfile/package manifest;
- filesystem;
- container image;
- IaC/config target.

Capture the Trivy version, target, scanners enabled, and package/file discovery counts when available.

## Fail-closed invariant
If the task expects dependencies and Trivy discovers zero packages, treat the scan as FAILED/BLOCKED. Never convert "nothing discovered" into "zero vulnerabilities."

## Findings
For each relevant finding capture:
- package/component;
- installed version;
- fixed version(s);
- vulnerability ID;
- severity;
- advisory/source;
- dependency path/reachability evidence when known.

## Remediation
Prefer the least disruptive version change that removes the vulnerability while respecting compatibility constraints. For transitives, use the ecosystem-native resolution mechanism.

## Verification
Re-run the same scan after remediation and verify:
1. the target/packages are still discovered;
2. the specific vulnerability is absent;
3. no material new vulnerability/regression was introduced.

A successful process exit alone is insufficient evidence if discovery was wrong.
