---
name: test-oracle-design
description: Design mechanical verification oracles for agentic/software changes, including expected artifacts, API/stream transcripts, failure cases, and measurable latency/error budgets.
---

# Test Oracle Design

## Purpose
Translate ambiguous acceptance language into evidence that can mechanically decide pass/fail.

## Oracle forms
Use the strongest applicable oracle:
- unit/integration/E2E assertion;
- schema or contract validation;
- golden file/snapshot where stable;
- API request/response transcript;
- SSE/stream event sequence transcript;
- state transition invariant;
- generated artifact/diff assertion;
- scanner finding count/identity;
- latency/error-rate/cost/token budget;
- post-deploy health check.

## Required fields
For each oracle capture:
- requirement/risk ID;
- setup/input;
- exact observation;
- pass condition;
- fail condition;
- command/tool;
- environment;
- tolerance/budget;
- evidence artifact.

## Rules
Avoid subjective "looks good" oracles. For streams, verify ordering, terminal events, errors, and reconnect/cancellation behavior as relevant. For budgets, define measurement window/sample size rather than one anecdotal request.

## Handoff
Implementation Design should reference oracle IDs; Gate C should consume observed results.
