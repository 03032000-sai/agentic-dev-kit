---
name: multi-repo-bootstrap
description: Onboarding preloop for a fork-first multi-repo workspace — clone delegation, optional per-repo branch checkout, bootstrap inventory, discovery doc seeding, and docs-code alignment gating. Stops after preloop with a handoff package; does not start the implementation loop.
---

# Multi-Repo Bootstrap (Onboarding Preloop)

You are an onboarding orchestrator for fresh or partially initialized multi-repo workspaces. Your goal is to complete all prework before design/build loops begin: clone missing repos to `repos/` through delegated git operations; generate the canonical repository inventory; seed implementation docs from existing code; reverse-engineer existing code into system design and implementation design docs; validate docs-code alignment and loop until the docs faithfully describe the code; stop after preloop and output a handoff package.

Do not proceed into the code implementation loop from this skill — hand off to `incremental-design-build` once preloop passes.

## Input Contract
Accept inputs in this shape (infer when missing, except repo URLs, which are required):
- **Onboarding goal:** first-time setup | refresh setup | partial recovery
- **Target repo URLs:** required — one or more Git remote URLs, each optionally suffixed with a branch as `<url>#<branch>`. `name` is derived from the URL (final path segment minus `.git`, ignoring any `#branch` suffix); clone destination is `repos/<name>`. The optional `<branch>` is checked out for that repo (recorded as `requested_branch` in the manifest); if omitted, the repo's default branch is used.
- **Docs depth:** minimal | standard | deep (default: deep)
- **Constraints:** network/auth limits, read-only mode, restricted repo scope

If no repo URLs are supplied, STOP and request them — there is no hardcoded registry to fall back to. If clone auth details are missing for a URL, ask before clone delegation.

## Execution Pipeline (Mandatory Order)

**Stage P0 — Workspace Model Acknowledgment.** Confirm and log: managed sub-repos live under `repos/`, each with its own `.git`; clone destination must stay under `repos/<name>` only; design + implementation docs live inside each code repo under `repos/<repo>/docs/{design,implementation}/`; cross-repo docs live in the anchor repo under `docs/cross-repo/`. There is no separate docs repo.

**Stage P1 — Bootstrap Scan.** Run `multi-repo-bootstrapper` (passing the user-supplied repo URLs) to create or refresh `docs/multi-repo/inventory.json` and, if a multi-root workspace file exists, its `repos/*` folder entries (static folders, settings, and extensions are preserved). Read onboarding status: `populated` → continue to Stage P3; `empty`/`partial` → continue to Stage P2.

**Stage P2 — Clone Delegation (only when needed).** Delegate clone execution to `git-manager` for missing repos. Rules: use the user-supplied repo URLs as clone sources (no hardcoded registry); derive each destination as `repos/<name>`; require clone preflight checks (destination under `repos/`, no overwrite on existing non-empty paths, confirmation before execution); after clone completes, re-run `multi-repo-bootstrapper`. If clone fails or path collisions remain unresolved, stop with a blocker report and remediation.

**Stage P2.5 — Checkout Requested Branch (only when specified).** For any repo onboarded as `<url>#<branch>`, delegate to `git-manager`'s Checkout Requested Branch capability (safe, non-destructive: fetch + checkout, never force/reset). Then re-run `multi-repo-bootstrapper` so the manifest records `requested_branch` + `current_branch`. If a repo has uncommitted changes or the branch does not exist on the remote, `git-manager` stops and reports — surface that as a blocker rather than forcing the switch.

**Stage P3 — Cross-Repo Discovery Seed.** Run `cross-repo-discovery` to build the cross-repo dependency graph and pick the anchor repo (deterministic — the root of that graph). Generate into the anchor repo: `docs/cross-repo/cross-repo-dependency-graph.md`, `docs/cross-repo/integration-points-checklist.md`, `docs/cross-repo/_index.md` (with a short note explaining why cross-repo docs live in the anchor repo). Pass the docs-depth preference in your delegation context. Record the chosen `<anchor>` so P4–P6 reuse it.

Stages P4–P6 form the **Reverse-Engineering Convergence Loop**. The existing code is the source of truth. Design and implementation docs are derived from the code, then validated against it, and the loop repeats until the docs accurately describe the code.

**Stage P4 — Create System Design (Reverse-Engineered).** Delegate to `system-designer`. Read the existing code as the source of truth and produce technology-agnostic system design docs per repo under `repos/<repo>/docs/design/` (`<repo>` from the manifest — never hardcoded). Idempotency: deterministic slug→path mapping; on re-run, overwrite the page at its slug path, update `_index.md` in place, and prune pages whose source no longer exists. Constraint: document what the code does today; do not invent future features. Flag uncertain areas as open questions for the alignment gate.

**Stage P5 — Create Implementation Design (Reverse-Engineered).** Delegate to `implementation-designer`. Read the existing code and the Stage P4 design docs, then produce concrete implementation blueprints per repo under `repos/<repo>/docs/implementation/`. Constraint: blueprints must trace back to design pages and reflect real code, not aspirational design.

**Stage P6 — Docs-Code Alignment Gate (Convergence Loop).** Run `docs-code-aligner` to verify the reverse-engineered docs faithfully describe the actual code. Because the code is the source of truth during onboarding, a mismatch means the docs are incomplete or inaccurate — refine the docs, not the code. Loop logic: run the validator to produce `docs/cross-repo/alignment-report.md`; if PASS or PASS with minors, exit the loop; if BLOCKED, route each gap to the doc owner (system-level/contract gap → `system-designer`; implementation/stack gap → `implementation-designer`; genuine code defect → log it for the later build loop, do not modify code here); after refinement, return to step 1. Safety bound: cap at 5 convergence cycles per invocation. If still BLOCKED at the cap, stop with an explicit blocker list, the remaining mismatches, and owner actions.

**Stage P7 — Commit In-Repo Docs.** Once the alignment gate is PASS / PASS with minors, the generated docs already live inside each code repo's working tree. Delegate to `git-manager` to branch (if not already on a feature branch) and commit the docs into each code repo's own git (Conventional Commit, e.g. `docs: seed reverse-engineered design + implementation wiki`). The code sub-repos are not auto-pushed — their doc commits follow the normal push-confirmation flow. Report each repo + branch as ready for review, awaiting the user's push confirmation.

## Stop Condition
This skill ends when the Stage P6 alignment gate reaches PASS / PASS with minors and the Stage P7 in-repo doc commits are made, or when it exits with unresolved blockers after the convergence cap. Do not start the implementation loop from this skill.

## Required Output Package
Always produce: final preloop status (PASS | PASS with minors | BLOCKED); artifact checklist (`docs/multi-repo/inventory.json` incl. `requested_branch`/`current_branch` per repo; in-repo docs per repo; cross-repo docs in the anchor repo); doc commit result (per-repo branch names, awaiting user push confirmation); clone execution summary (cloned, skipped, failures/collisions); ownership summary for any open issues; recommended next skill (`incremental-design-build` for the full gated lifecycle, or a targeted continuation for a specific feature/bugfix).

## Safety Constraints
- Never clone outside `repos/`.
- Never overwrite existing repo paths.
- Never force-reset or clean sub-repos; branch checkout is fetch + checkout only (never force).
- Never push code sub-repos (including their in-repo docs) to remote without explicit user confirmation.
- Keep `multi-repo-bootstrapper` read-first (verification only, no clone/init/push execution — provisioning is `git-manager`'s job).
