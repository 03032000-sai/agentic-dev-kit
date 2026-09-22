---
name: enterprise-package-routing
description: Configure private/public package-source routing safely across Python, npm, Maven/Gradle, and .NET without embedding credentials.
---

# Enterprise Package Routing

## Mission
Resolve packages from the correct private/public registries while preserving credential safety and reproducibility.

## General rules
- repository config may define registry URLs, but secrets/tokens belong in environment variables, credential helpers, CI secrets, or platform-native auth;
- never commit plaintext credentials;
- distinguish publish registry from install registry;
- fail clearly when the required private source is unavailable instead of silently pulling a similarly named public package;
- preserve lockfile integrity.

## Python
Use project/tool-supported indexes/sources. Be explicit about primary vs supplemental index behavior to reduce dependency-confusion risk.

## npm/pnpm/yarn
Use scope-specific registry mapping where possible. Keep auth tokens out of committed `.npmrc`.

## Maven/Gradle
Keep repository definitions separate from credentials; use settings/credential providers/CI secrets according to project conventions.

## .NET
Use NuGet source mapping or equivalent where supported; credentials remain external to committed config.

## Validation
Resolve a known private package, a known public package, and verify the effective dependency graph/lockfile without exposing credentials in logs.
