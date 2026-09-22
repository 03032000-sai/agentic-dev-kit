# Chat Usage Cheat Sheet

## GitHub Copilot
Select a custom role from the Agent picker, or run a workflow from the prompt-file picker.

## Claude Code
Use `/agents` to inspect roles.
Examples:
`/incremental-design-build Add pagination`
`/bugfix Fix duplicate notifications`
`/knowledge-discovery Explain authentication`

## Codex
Examples:
`$incremental-design-build Add pagination`
`$bugfix Fix duplicate notifications`
`$knowledge-discovery Explain authentication`

Recommended everyday mapping:
feature/non-trivial change → incremental-design-build
bug → bugfix
unknown repo → brownfield-bootstrap
architecture question → knowledge-discovery
refactor → safe-refactor
security issue → security-remediation
release → release-readiness
