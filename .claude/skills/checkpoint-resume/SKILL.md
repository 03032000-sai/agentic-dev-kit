---
name: checkpoint-resume
description: Safely resume a long-running agentic task from a durable checkpoint by verifying repository state, SHA drift, approved artifacts, findings, and next-role authority before mutation.
---

# Checkpoint Resume

## Read first
Load the durable checkpoint and referenced Change Brief/artifacts.

## Verify reality
Compare checkpoint to current:
- repository root/remote;
- branch;
- HEAD SHA;
- dirty state;
- current stage/gate;
- referenced files/artifacts.

## Drift handling
If HEAD, branch, or material files changed after the checkpoint:
1. do not mutate;
2. classify the drift;
3. determine which design/review/validation evidence is stale;
4. refresh the affected evidence or route back to the responsible gate;
5. update checkpoint only after reconciliation.

## Resume packet
Produce:
- checkpoint validity: valid | stale | corrupt | incomplete;
- current repo fingerprint;
- approved artifacts still valid;
- findings still open;
- ordered next steps;
- recommended next agent;
- mutation ownership.

## Fail-safe
A corrupt/untrusted checkpoint forces read-only planning until durable state is restored.
