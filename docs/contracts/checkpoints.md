# Durable Checkpoint Contract

Durable checkpoints make long-running agent work resumable across compaction, session changes, model changes, and specialist-agent handoffs.

Recommended location:

```text
.agents/checkpoints/<sanitized-branch>/checkpoint.yaml
```

A repository may configure another location, but the location must be branch-safe and deterministic.

## Schema

```yaml
checkpoint_version: 1

repository:
  name:
  root:
  remote:

git:
  branch:
  head_sha:
  base_branch:

change_brief:
  path:
  goal:
  definition_of_done: []

current_stage:
current_gate:

approved_artifacts:
  system_design:
  implementation_design:

changed_files: []
documentation_changed: []

validation:
  - command:
    working_directory:
    result: pass | fail | blocked | not_run
    summary:
    timestamp:

critic_findings:
  blocking: []
  important: []
  advisory: []

risks: []
blockers: []

ordered_next_steps: []
recommended_next_agent:

context:
  key_decisions: []
  unresolved_questions: []
  files_that_must_be_reloaded: []
```

## Write points

Update the checkpoint:
- after Stage 0;
- after an approved design artifact;
- after each meaningful implementation iteration;
- after local validation;
- after clean-context validation;
- after a gate decision;
- before intentional context compaction or session termination.

## Failure behavior

If the checkpoint cannot be written, parsed, or trusted:
1. stop mutation;
2. preserve the current working-tree state;
3. switch to read-only planning/diagnosis;
4. restore durable state before continuing implementation.

Do not continue mutable work using only conversational memory.
