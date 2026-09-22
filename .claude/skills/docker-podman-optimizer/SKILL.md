---
name: docker-podman-optimizer
description: Optimize Dockerfiles and compose files for build-cache efficiency across Docker and Podman.
---

# Docker/Podman Optimizer
Order Dockerfile instructions from least to most frequently changing so layer caching survives normal iteration; copy dependency manifests and install before copying source. Use multi-stage builds to keep the final image free of build-only tooling. Use BuildKit cache mounts (`--mount=type=cache`) for package manager caches instead of baking them into layers. Verify the optimization actually reduces rebuild time before treating it as done — measure, don't assume.
