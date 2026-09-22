# GitHub Copilot Repository Instructions

Read `/AGENTS.md` as the canonical operating contract.

For substantial engineering tasks:
- investigate before editing;
- use specialized custom agents from `.github/agents/`;
- use prompt files in `.github/prompts/` as workflow entry points;
- use skills under `.agents/skills/` when relevant;
- keep design, implementation, and independent critique distinct;
- use deterministic validation before completion;
- surface uncertainty and failed checks explicitly;
- do not perform destructive or production-impacting operations without explicit approval.

For features and non-trivial fixes, prefer the `incremental-design-build` workflow. For multi-repo work, start with `multi-repo-bootstrap`; for business-facing documentation, use `business-docs-loop`.
