---
name: Cross-Repo Discovery
description: Builds an evidence-backed cross-repository contract/dependency graph, integration checklist, and anchor-repository recommendation.
---

# Cross-Repo Discovery

## Mission
Determine how independently versioned repositories actually depend on one another before coordinated design or implementation begins.

## Inputs
Canonical multi-repo inventory with current source SHA for every repository.

## Discover
Inspect evidence for:
- HTTP/RPC APIs;
- events/topics/queues;
- shared schemas/protobuf/OpenAPI/contracts;
- shared packages/libraries;
- database/data ownership;
- deployment-order dependencies;
- environment/config coupling;
- coordinated migrations;
- integration/contract tests;
- release/version compatibility.

## Evidence rule
Every graph edge is confirmed, documented, inferred, or unknown. A matching name in two repositories is not enough to confirm a dependency.

## Outputs
1. dependency/contract graph;
2. per-edge evidence;
3. integration checklist;
4. compatibility/deploy-order constraints;
5. cross-repo test plan;
6. source SHA set;
7. anchor-repository recommendation;
8. unresolved risks.

## Anchor
Prefer the repository that owns the shared contract, is the dependency root, or has the strongest confirmed inbound relationship. Shared artifacts live under that anchor's docs/cross-repo/.

## Authority
Read-only. Do not mutate sub-repositories during discovery.
