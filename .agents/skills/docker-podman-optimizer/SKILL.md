---
name: docker-podman-optimizer
description: Optimize Dockerfiles and container build configurations, prioritizing layer caching first, followed by build context efficiency, BuildKit support, multi-stage builds, and cross-platform compatibility in descending order of importance. Use when writing Dockerfiles, docker-compose files, build scripts, CI/CD pipelines, or infrastructure-as-code for container builds.
---

# Docker & Podman Build Optimizer

This skill ensures generated Dockerfiles and container build configurations follow industry best practices for: layer caching (minimize rebuild times when dependencies don't change); build context size (exclude unnecessary files to speed context transfer); BuildKit optimization (leverage modern Docker/Podman build features); multi-stage efficiency (separate concerns into independent build targets); cross-platform compatibility (host development vs. Linux container targets).

If a higher-priority optimization (layer caching) conflicts with a lower-priority one (multi-stage build structure), favor the higher-priority optimization.

## When to Use
Apply this skill when writing: Dockerfiles (any language); `docker-compose.yml` / `docker-compose.prod.yml`; build scripts that invoke `docker build` or `podman build`; CI/CD pipeline steps that build container images; Infrastructure-as-Code that defines build behavior.

Do NOT apply when pulling pre-built images (no changes needed), or writing non-container build logic (Maven, Gradle, Webpack, etc.).

## Core Principles

**1. Split dependency install from source copy.**
Bad: `COPY . .` then `RUN npm install` — any source change invalidates the entire install layer.
Good:
```dockerfile
COPY package.json package-lock.json ./
RUN npm install
COPY . .
```
Dependencies are reinstalled only when `package*.json` changes.

**2. Use BuildKit cache mounts.**
```dockerfile
# syntax=docker/dockerfile:1
FROM node:22-alpine
COPY package.json package-lock.json ./
RUN --mount=type=cache,id=npm-cache,target=/root/.npm \
    npm ci --prefer-offline --no-audit --no-fund
```
```dockerfile
# syntax=docker/dockerfile:1
FROM python:3.12-slim
COPY requirements.txt ./
RUN --mount=type=cache,id=pip-cache,target=/root/.cache/pip \
    pip install --prefer-binary -r requirements.txt
```
Benefits: cache persists across builds without baking into image layers; only new/changed packages are downloaded; works with both Docker and Podman (`DOCKER_BUILDKIT=1` / `PODMAN_BUILDKIT=1`); does not increase final image size. Requires `# syntax=docker/dockerfile:1` at the top and BuildKit enabled in the build command or CI environment.

**3. Multi-stage builds with distinct targets.**
```dockerfile
# Stage 1: deps
FROM node:22-alpine AS deps
COPY package.json package-lock.json ./
RUN npm ci

# Stage 2: dev
FROM node:22-alpine AS dev
COPY --from=deps /app/node_modules ./node_modules
COPY . .
CMD ["npm", "run", "dev"]

# Stage 3: test
FROM dev AS test
CMD ["npm", "test"]

# Stage 4: builder
FROM dev AS builder
RUN npm run build

# Stage 5: runtime
FROM node:22-alpine AS runtime
COPY --from=builder /app/dist ./dist
RUN npm ci --omit=dev
CMD ["node", "dist/index.js"]
```
Benefits: local dev builds are small and fast (`podman build --target dev`); test and production targets are independent; the final production image excludes dev dependencies and build artifacts.

**4. Create `.dockerignore` at root & layer roots.** Content template:
```
node_modules
npm-debug.log
.git
.gitignore
.DS_Store
.vscode
.idea
coverage
dist
build
.tmp
.cache
.env
*.local
__pycache__
*.pyc
.pytest_cache
.mypy_cache
*.egg-info
.coverage
```
Reduces build context size by 50-80%, reduces cache invalidations, speeds context transfer, and — critically — `.env`/`*.local` prevent secrets from leaking into images.

**5. Use package manager lock files.** Node.js: always `npm ci` instead of `npm install`. Python: pin versions in `requirements.txt`/`pyproject.toml`. Ensures reproducible builds, works well with cache mounts, and is faster on repeated builds (no resolution phase).

**6. Leverage layer caching order** (expensive → cheap, in execution order): base image pull; system dependencies (`apt-get install`, `apk add`); application build tools; application dependencies (`package.json`, `requirements.txt`); application source code (changes most frequently).

**7. Context configuration for docker-compose** (development):
```yaml
services:
  ui:
    build:
      context: .
      target: dev
    volumes:
      - ./src:/app/src
      - ui_node_modules:/app/node_modules
    command: npm run dev

volumes:
  ui_node_modules:
```
Source binds from the host for live reload; `node_modules` lives in a named volume so Linux modules aren't masked by host modules.

## Language-Specific Patterns

**Node.js / npm:**
```dockerfile
# syntax=docker/dockerfile:1
FROM node:22-alpine
WORKDIR /app
COPY package.json package-lock.json ./
RUN --mount=type=cache,id=npm-cache,target=/root/.npm \
    npm ci --prefer-offline --no-audit --no-fund
COPY . .
RUN npm run build
CMD ["node", "dist/index.js"]
```

**Python (pip):**
```dockerfile
# syntax=docker/dockerfile:1
FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt ./
RUN --mount=type=cache,id=pip-cache,target=/root/.cache/pip \
    pip install --prefer-binary -r requirements.txt
COPY src/ ./src/
ENV PYTHONPATH=/app/src
CMD ["python", "-m", "myapp"]
```
Use `--prefer-binary` to avoid compiling from source when a binary wheel is available; use `--mount=type=cache` instead of `--no-cache-dir`.

**Go:**
```dockerfile
# syntax=docker/dockerfile:1
FROM golang:1.22-alpine AS builder
WORKDIR /src
COPY go.mod go.sum ./
RUN --mount=type=cache,id=go-cache,target=/root/go/pkg/mod \
    go mod download
COPY . .
RUN CGO_ENABLED=0 go build -o /app/myapp .

FROM alpine:latest
COPY --from=builder /app/myapp .
CMD ["./myapp"]
```

## Common Mistakes & Fixes
| ❌ Mistake | ✅ Fix |
|---|---|
| `COPY . .` before dependency install | Move to end: copy manifest → install → `COPY . .` |
| `pip install --no-cache-dir` | Use `--mount=type=cache` + remove `--no-cache-dir` |
| No BuildKit syntax declaration | Add `# syntax=docker/dockerfile:1` at top |
| `.env` files in git / image | Add to `.dockerignore`; use `RUN --mount=type=secret` for secrets |
| Copying host `node_modules` to Alpine | Never do this; install inside the container |
| Large build context (10+ GB) | Create `.dockerignore` with `node_modules`, `.git`, etc. |
| All-in-one Dockerfile, no stages | Use multi-stage: `deps`, `dev`, `runtime` |

## Validation Checklist
Before submitting any Dockerfile or build config: `# syntax=docker/dockerfile:1` present if using cache mounts; dependencies copied before source code; cache mounts present for expensive installs (npm, pip, apt-get); `.dockerignore` exists at project root; multi-stage build has distinct targets (`deps`, `dev`/`test`, `builder`, `runtime`); `docker-compose.yml` specifies `target: dev` for local development; no direct copying of host `node_modules`/site-packages; secrets are NOT in the Dockerfile or excluded from `.dockerignore`; final image size is reasonable.

## Integration with Implementer
When writing container build logic: reference this skill explicitly ("Applying docker-podman-optimizer skill"); follow the multi-stage + cache mount pattern for all Dockerfiles; create `.dockerignore` at appropriate levels; document build targets in comments (e.g., `# build with --target dev`); validate against the checklist before marking the task complete.
