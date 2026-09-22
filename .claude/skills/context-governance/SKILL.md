---
name: context-governance
description: Keep long agent workflows reliable through progressive disclosure, fresh-context critique, compaction, and durable checkpoints.
---

# Context Governance

Treat model context as a finite engineering resource.

## Load order
1. repository instructions + current checkpoint;
2. indexes/manifests/metadata;
3. task-relevant files/symbols;
4. direct dependencies/callers;
5. deeper transitive evidence only when needed.

## Keep
- current Change Brief and DoD;
- approved decisions/artifacts;
- authoritative evidence references;
- current findings;
- validation state;
- ordered next steps.

## Drop/compact
- superseded exploration;
- repeated raw logs once summarized with path/reference;
- old author narrative;
- irrelevant files;
- resolved alternatives.

## Fresh critic rule
A critic receives the requirement, artifact, and minimum authoritative evidence—not the full author transcript.

## Checkpoint triggers
Checkpoint after Stage 0, each gate pass/fail, meaningful implementation iteration, validation phase, and before compaction/session handoff.

## Safety threshold
Do not deliberately run context to exhaustion. If context is becoming dominated by stale material, checkpoint and start the next stage from the compact durable state.

## Failure rule
If durable state cannot be trusted, stop mutation and use read-only planning until restored.
