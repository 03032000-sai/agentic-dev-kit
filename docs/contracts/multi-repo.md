# Multi-Repo Contract

## Sub-Repo Input Contract
The managed sub-repo set is not hardcoded. It is supplied by the user as a list of Git remote URLs at trigger time. The bootstrap flow derives everything else from those URLs.

- The user passes one or more Git remote URLs when triggering `multi-repo-bootstrap` or a design-build skill. Example: `https://github.com/<org>/<project>.git`.

## Name Derivation
- `name` = the final path segment of the URL with any trailing `.git` removed. E.g. `https://github.com/acme/my-service.git` → `my-service`.
- `path` = `repos/<name>` (the clone destination, always under `repos/`).
- `default_branch` = the remote's `origin/HEAD` detected after clone; if undetectable, default to `main`.

## Per-Repo Branch Selection (Optional)
- A URL may carry an optional branch as `<url>#<branch>` (e.g. `https://github.com/acme/svc.git#develop`).
- Split the `#<branch>` suffix before deriving `name` (the suffix never affects name/path).
- Record the branch as `requested_branch` in the manifest (null when absent).
- The branch is checked out by `git-manager` via fetch + checkout, never force/reset; the bootstrapper only records `requested_branch` and the observed `current_branch`. The incremental loop bases its `feature/*`/`fix/*` branches off the chosen branch.

## Collision Handling
If two URLs derive the same name, this is an error. Stop and require the user to disambiguate with an explicit alias: `<url> as <alias>`.

## No Fallback (Mandatory)
If no URLs are provided at trigger time, the bootstrap flow stops with an error and requests URLs. There is no hardcoded registry, filesystem scan, or manifest used as a source for the repo set. A previously written manifest or an existing `repos/` checkout may be consulted only to report status (is `repos/<name>` already cloned?), never to supply the canonical set.

## Where Docs Live (In-Repo)
Design + implementation docs are not a separate repository. They live inside each code repo under `repos/<repo>/docs/{design,implementation}/`, beside that repo's existing `docs/`. Cross-repo artifacts (dependency graph, integration checklist, system overview, alignment report) live in the anchor repo (the root of the cross-repo dependency graph) under `docs/cross-repo/`.

Because docs live inside the code repo, they ride the code's git branch automatically — no separate docs repo, no docs branch, no extra remote. The wrapper's `.gitignore` still excludes all of `repos/`; doc changes commit to their code repo's git.

## Manifest Schema
**Location:** `docs/multi-repo/inventory.json`

```json
{
  "bootstrap_timestamp": "2026-06-15T14:30:00Z",
  "bootstrap_method": "user_input",
  "wrapper_repo": {
    "path": "/absolute/path/to/<wrapper-repo>",
    "git_remote": "<wrapper-origin-url-or-local-only>",
    "current_branch": "main"
  },
  "managed_subrepos": [
    {
      "name": "<derived-from-url>",
      "path": "repos/<derived-from-url>",
      "remote": "<user-supplied-url>",
      "default_branch": "main",
      "requested_branch": "<branch from <url>#<branch> or null>",
      "status": "cloned | not-cloned | corrupted",
      "current_branch": "main",
      "git_root": "/absolute/path/to/repos/<derived-from-url>/.git"
    }
  ],
  "onboarding_status": "empty | partial | populated",
  "onboarding_message": "Descriptive status for downstream agents"
}
```

**Field definitions:** `bootstrap_timestamp` — ISO-8601 when the manifest was generated. `bootstrap_method` — always `user_input` (filesystem or workspace-file scans may inform per-repo status only, never the set itself). `wrapper_repo.path` — absolute path to the workspace root. `wrapper_repo.git_remote` — result of `git remote get-url origin`, or `"local-only"` if no remote. `managed_subrepos[].requested_branch` — the branch requested via `<url>#<branch>`, or null; checked out by `git-manager` (fetch + checkout, never force). `managed_subrepos[].current_branch` — the branch actually checked out after bootstrap. `managed_subrepos[].status` — `cloned` (`.git` exists, remote matches, git commands succeed), `not-cloned` (directory/`.git` missing), or `corrupted` (`.git` exists but remote mismatches or git commands fail). `onboarding_status` — `empty` (none cloned), `partial` (some cloned), `populated` (all cloned).

## Checkout / Refresh Semantics

**Initial bootstrap (empty `repos/`):** run `multi-repo-bootstrapper` with the user-supplied URLs → it detects `onboarding_status: empty` and emits clone instructions → clone the repos (manual or delegated via `git-manager`) → re-run `multi-repo-bootstrapper` to confirm → proceed to `cross-repo-discovery`.

**Refresh existing checkouts:** on every loop run, run `multi-repo-bootstrapper` to read current state. If the manifest is fresh (< 1 hour old), skip refresh and reuse it. If stale or missing, re-run, check for stale branches or unpushed commits, and report findings to the user — never force-checkout or reset sub-repo branches automatically.

## Guardrails (Non-Negotiable)

1. **No force-clone.** The bootstrapper never runs `git clone` automatically. Cloning is executed only by explicit user action. Rationale: sub-repos may have local work in progress; avoid data loss.
2. **No force-reset.** The bootstrapper never runs `git reset --hard`, `git clean -fd`, or equivalent. If a sub-repo is dirty, report status and ask the user to resolve manually. Rationale: preserve local development state.
3. **No branch auto-checkout.** The bootstrapper does not automatically `git checkout` a different branch. If a sub-repo is on a non-default branch, report it as informational. Rationale: preserve explicit user workflow.
4. **No remote authority.** The bootstrapper does not fetch or pull from remote automatically. The user is responsible for pulling before running discovery. Rationale: avoid implicit network I/O and credential overhead.
5. **Portable roots.** The managed repo set comes from user-supplied URLs; any workspace-file or `repos/*/` scan is used only to report per-repo status, never to source the set. Hardcoding repo names, remotes, or paths in skills or agents is forbidden — use placeholder patterns like `repos/<name>/` or read from the manifest.
6. **Explicit URL input — no fallback.** The bootstrap flow requires one or more Git remote URLs at trigger time. If none are supplied, stop with an error. Never substitute a hardcoded list, a prior manifest, or an existing `repos/` checkout as the canonical set. Rationale: keep the flow fork-agnostic and reproducible across any set of repositories.

## Git Separation
The wrapper repository tracks only the agent engine (agents/skills/prompts/contracts). Sub-repos under `repos/<name>/` each keep their own independent `.git`, remote, and branch. `git-manager` operations target one or the other, never both in the same command.

## Onboarding First-Time Flow
1. User checks out the wrapper repo.
2. User runs `multi-repo-bootstrap` with one or more repo URLs.
3. `multi-repo-bootstrapper` reads the URL set; if none supplied, it stops and requests URLs.
4. `multi-repo-bootstrapper` detects `onboarding_status: empty` and emits clone instructions.
5. User executes the clone flow (directly or via `git-manager`).
6. User re-runs Stage 0 bootstrap.
7. `multi-repo-bootstrapper` confirms `populated` status.
8. `cross-repo-discovery` runs.
9. The design-build loop proceeds.

## Non-Goals
- Automatically updating submodules or git subtrees.
- Enforcing branch naming conventions (that's `git-manager`'s job).
- Managing CI/CD pipeline orchestration.
