---
name: docker-podman-optimizer
description: Optimize Docker/Podman builds for reproducibility, cache efficiency, small images, and host/container isolation.
---

# Docker / Podman Optimizer

## Goals
Improve container builds without changing application semantics.

## Principles
- keep dependency resolution inside the container unless host/container compatibility is proven;
- order Dockerfile steps to maximize stable cache reuse;
- use multi-stage builds when build/runtime dependencies differ;
- copy dependency manifests before source where that enables cache reuse;
- avoid copying host `node_modules`, virtualenvs, build caches, or credentials into images;
- use `.dockerignore` aggressively;
- pin base images according to repository policy;
- preserve non-root runtime where supported.

## Cache strategy
Prefer BuildKit/Podman cache mounts for package-manager caches when the build engine supports them. Do not blindly combine "disable all caches" guidance with build-layer optimization.

## Validation
Compare:
- clean build success;
- rebuild with unchanged dependencies;
- image size/layers;
- runtime smoke test;
- non-root/permissions;
- dependency reproducibility.

## Conflict rule
When host reuse conflicts with container-native dependency integrity, container-native wins unless compatibility is demonstrated.
