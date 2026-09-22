---
name: replay-debugging
description: Debug stateful or agentic workflows by replaying persisted inputs, checkpoints, events, and tool results to isolate the first deterministic divergence.
---

# Replay / Time-Travel Debugging

## Use when
A workflow is stateful, checkpointed, event-driven, or agentic and a failure cannot be understood reliably from the final error alone.

## Evidence sources
Prefer persisted:
- input/request envelope;
- workflow/run ID;
- checkpoint/state snapshots;
- event or message sequence;
- tool invocations/results;
- model/provider metadata when relevant;
- retry/cancellation events;
- candidate/source SHA;
- timestamps/correlation IDs.

Never reconstruct missing execution history from model imagination.

## Method
1. Pin the failing run and code/config SHA.
2. Build an ordered execution timeline.
3. Identify the last known-good checkpoint/state.
4. Replay from the earliest reproducible boundary using deterministic or stubbed external inputs where possible.
5. Compare expected vs observed state after each transition.
6. Isolate the **first divergence**, not merely the final symptom.
7. Classify divergence source: input, state transition, tool/dependency, retry/order, model nondeterminism, configuration, or code.
8. Add a replay/regression oracle before remediation when feasible.

## Time travel
If the host framework supports checkpoint restore/time-travel, use it to branch from an earlier state without overwriting original evidence. Keep the original run immutable.

## Nondeterministic components
Record prompts/model/config/tool versions and control stochasticity when the platform permits. If exact replay is impossible, distinguish deterministic state replay from nondeterministic model re-execution.

## Safety
Replay must not re-trigger destructive production side effects. Stub/sandbox external writes or use read-only tools unless explicitly approved.

## Output
Timeline, checkpoint comparison, first-divergence evidence, root-cause confidence, replay oracle, and recommended responsible stage.
