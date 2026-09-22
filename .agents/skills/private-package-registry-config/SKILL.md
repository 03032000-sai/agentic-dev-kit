---
name: private-package-registry-config
description: Configure an organization's private/internal package registry for Python (pip.conf), npm (.npmrc), Maven (settings.xml), Gradle repositories, .NET NuGet.Config, and Docker builds. Use when a developer or automated system needs to route package installs through an internal registry mirror instead of public registries, or wants faster frontend debug loops that avoid rebuilding containers for every dependency change.
---

# Private Package Registry Configuration

## What This Skill Does
This skill standardizes how coding agents configure package repositories and dependency-installation flows for an organization that hosts its own internal package registry (a common enterprise pattern — e.g. a Nexus, Artifactory, or Verdaccio mirror). It covers: Python installs through an internal PyPI proxy; npm installs through an internal npm registry; Maven builds through an internal `settings.xml`; Gradle builds using the same internal Maven endpoints and credentials model; .NET/NuGet package restores through an internal NuGet proxy; Docker build patterns that preserve these repository settings; faster frontend debug cycles by preferring a local `npm install` and copying/mounting `node_modules` instead of repeating non-incremental Docker dependency installs.

## When to Use
Use this skill on any project that needs to route through an internal package registry instead of public defaults, especially if the workspace contains: `pyproject.toml`, `requirements.txt`, or Dockerfiles that install Python packages; `package.json` or frontend containers that run `npm install`; `pom.xml`, `settings.xml`, `build.gradle`, or `build.gradle.kts`; `.csproj`, `.fsproj`, `.sln`, `NuGet.Config`, or Dockerfiles that run `dotnet restore`; container build steps that currently fail because they resolve against public package registries instead of the internal mirror.

## Core Rules
- Prefer the organization's internal registry over public defaults when the project is expected to build inside the organization's network.
- Do not commit plaintext credentials. Use environment variables, mounted secret files, CI variables, or existing local machine settings.
- If a user gives you a fully materialized local credentials file, you may use it locally for commands, but do not copy secrets into committed workspace files.
- For frontend debug loops, prefer a local `npm install` and then copy or mount `node_modules` into the debug container or compose service rather than rebuilding the image for every dependency change.
- Preserve incremental install layers in Dockerfiles unless the build process explicitly requires a full rebuild.

## Repository Endpoints (placeholders — substitute your organization's actual registry)

**Python / pip:**
```ini
[global]
index-url = https://<internal-registry-host>/repository/pypi-proxy/simple
trusted-host = <internal-registry-host>
```

**Python / uv:**
```toml
[[tool.uv.index]]
url = "https://<internal-registry-host>/repository/pypi-proxy/simple"
default = true
```

**npm:**
```ini
registry=https://<internal-registry-host>/repository/npm-registry/
always-auth=false
```

**Maven:** use a `settings.xml` aligned with your organization's internal mirrors, servers, and repositories.

**Gradle:** Gradle does not automatically consume Maven's `settings.xml` the way Maven does — mirror the same repository URLs and credential model in Gradle repository declarations or an init script.

**.NET / NuGet:**
```
https://<internal-registry-host>/repository/nuget.org-v3/index.json
```

## Procedure

**1. Detect active package ecosystems.** Inspect the project for: Python (`pyproject.toml`, `requirements.txt`, `requirements-dev.txt`, `pip.conf`, Dockerfiles); Node.js (`package.json`, `.npmrc`, Dockerfiles, compose files); Java (`pom.xml`, `settings.xml`, `build.gradle`, `build.gradle.kts`, `gradle.properties`); .NET (`.csproj`, `.fsproj`, `.sln`, `NuGet.Config`, `global.json`, Dockerfiles). If a required config file is missing or incomplete, generate a default template and inform the user. For multi-ecosystem projects, apply the relevant configuration for each without conflicts.

**2. Apply ecosystem-specific configuration.**

*Python:* prefer a workspace or image-level `pip.conf`. For Docker builds, copy `pip.conf` into `/etc/pip.conf` before running package installation. If the project uses requirements files, ensure install commands honor the proxy configuration rather than the default public index.
```dockerfile
COPY pip.conf /etc/pip.conf
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
```

*npm:* add/update `.npmrc`; run `npm install` locally during active debug cycles; for containerized frontend debugging, copy or mount the resulting `node_modules` into the container rather than re-running dependency resolution on every rebuild. Preferred debug-cycle pattern: install on the host, reuse the installed `node_modules` in the container via copy/bind mount/compose volume, and rebuild the container only when the runtime image itself changes materially.

*Maven:* create a local `settings.xml` from your organization's template; replace credential placeholders with environment-variable-backed values or user-local secrets; invoke Maven with `-s /path/to/settings.xml` when the project doesn't already use the correct settings file; keep the internal mirror IDs and repository URLs aligned with the template unless a different internal topology is requested.

*Gradle:* do not assume Maven's `settings.xml` alone is enough; use an init script or repositories block that mirrors the same internal endpoints; source credentials from environment variables or `gradle.properties`, not committed plaintext; prefer a shared configuration block or init script if multiple subprojects need the same repository settings; when invoking from CI, pass the init script explicitly with `-I init.gradle`.

*.NET/NuGet:* place/update a `NuGet.Config` at the solution root or a user-level location; the `<clear />` directive ensures only the internal proxy is used, preventing accidental fallback to the public registry; for Docker builds, copy `NuGet.Config` into the image before `dotnet restore`:
```dockerfile
COPY NuGet.Config ./
RUN dotnet restore
```
If credentials are required for the internal NuGet feed, add them via environment variables or a CI secret rather than committing them.

**3. Optimize Docker layering.** Copy repo config files before dependency installation; copy dependency manifests before application source to preserve cache reuse; avoid full image rebuilds solely to refresh frontend dependencies during tight debug loops when a host-side install plus copied/mounted `node_modules` is sufficient.

## Decision Points
- Build runs only on a developer workstation → local user-level settings may be enough.
- Build runs in CI or Docker → copy the config into the image or mount it explicitly.
- npm dependency iteration is the slow step → switch to local `npm install` plus copied/mounted `node_modules` for the debug cycle.
- Gradle is used → configure Gradle repositories directly instead of relying on Maven behavior.
- .NET is used → place `NuGet.Config` at the solution root and ensure `<clear />` is present.
- User explicitly provides secrets → use them for local execution only; never write them into tracked files.

## Completion Checks
A configuration is complete only when: dependency installs resolve through the intended internal registry endpoints; no newly created tracked file contains plaintext credentials; Dockerfiles preserve incremental cache behavior around dependency installation; frontend debug loops avoid unnecessary full rebuilds when local `npm install` is viable; Maven commands use the intended `settings.xml`; Gradle builds point at the equivalent internal repositories; `dotnet restore` resolves packages from the internal NuGet proxy, not the public registry directly.

## Common Fixes
- Python still hits the public registry → verify `pip.conf` is copied into the image before `pip install` runs.
- npm still resolves publicly → verify the workspace/image contains the expected `.npmrc`.
- Maven ignores the template → pass `-s` explicitly.
- Gradle cannot resolve dependencies → add explicit `repositories` entries; Gradle does not inherit Maven settings automatically.
- `dotnet restore` fails to resolve packages → verify `NuGet.Config` is present at the solution root with the internal feed URL.
- Frontend debugging is slow → stop rebuilding the image for every `npm install`; reuse host-installed dependencies during the loop.
