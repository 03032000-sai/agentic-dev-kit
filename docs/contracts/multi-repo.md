# Multi-Repo Contract

## Manifest
Canonical inventory lives at `docs/multi-repo/inventory.json`: one entry per sub-repo with `name`, `source_url`, `requested_branch`, `current_branch`, `path` (`repos/<name>`).

## Name derivation
`<name>` is the URL's final path segment with `.git` stripped, unless the user supplies an explicit alias.

## Git separation
The wrapper repository tracks only the agent engine (agents/skills/prompts/contracts). Sub-repos under `repos/<name>/` each keep their own independent `.git`, remote, and branch. Git Manager operations target one or the other, never both in the same command.

## Guardrails
Never force-clone over an existing non-empty destination. Never force-checkout, reset --hard, or discard uncommitted changes in a sub-repo without explicit approval. Resolved destination paths must stay under `repos/` — block path traversal.
