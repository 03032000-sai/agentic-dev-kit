# Business-Docs Loop — Shared Contract

This document is the single source of truth for how the Business-Docs Loop turns a selected repository's code into business documentation for non-technical business analysts (BAs). Every worker and critic agent in this loop obeys it. It is deliberately opinionated: the whole value of the loop is that a BA can trust what it produces.

## 1. The Comprehension Model — AI-Led, Deterministically Verified ("trust, but verify")

The AI is the author. A capable model reads the actual code and writes the business understanding in its own words. Understanding meaning, capabilities, and narratives requires reading real code — a parser cannot do it.

A deterministic layer sits underneath as a safety net only. It has exactly three jobs and it never writes a business claim:
- **Coverage checklist** — mechanically enumerate what exists (endpoints, data stores, jobs, screens, rule-candidate sites) so we can flag what the AI skipped.
- **Citation verifier** — for every claim the AI makes, confirm the cited code location exists and actually contains what the claim says. If it does not → the claim is flagged/rejected, never published.
- **Supportive facts appendix** — publish the hard inventory beside the narrative as grounding.

Canonical flow (every worker agent follows it): AI reads real code → writes the understanding in plain business language → attaches a code citation to every claim → the verifier confirms each citation is real and matches → the coverage check confirms nothing material was skipped.

The deterministic layer can reject or flag a claim; it can never write one. The AI can never emit a business claim without a verifiable citation.

### 1.1 The deterministic layer is a real check, not a promise
"Deterministically verified" means concrete, non-LLM checks — run by `business-doc-publisher` and re-run by the critics at each gate, all fail-closed:
- **Coverage scan** — a structural scan of the pinned checkout that enumerates the inventory (routes via the app's OpenAPI or route decorators; ORM models & fields; IaC-declared tables/queues/topics; route tables & literal HTTP call sites; scheduled/queue jobs; domain-quantity conditionals as rule-candidate sites). This inventory is the coverage denominator (§9).
- **Citation verifier** — for every evidence envelope (not a sample): resolve path·symbol at the pinned SHA, recompute the content hash, and confirm the cited code semantically supports the specific values/conditions/transition asserted (not merely that the symbol exists). A citation that does not resolve, whose hash drifted, or whose code contradicts the claim → rejected.
- **Prose linters** — readability and the jargon/identifier lint over `business-docs/**` (§10).

Critics perform the same resolution independently; the publisher performs the full 100% pass before publish. No gate passes on "spot-check only."

## 2. WHAT vs. WHY — the Hard Wall (Non-Negotiable)

Code can prove what a system does. It can almost never prove why the business does it.

| Kind of statement | Example | Allowed confidence |
|---|---|---|
| WHAT — behavior read in code, citation verified | "A single transfer is rejected when the amount exceeds 10,000." | Confirmed |
| WHY / intent — the business reason, even a strong inference | "…because of an anti-money-laundering limit." | Inferred — needs SME (never Confirmed) |

A business-purpose/intent claim is structurally capped at `inferred`. It may only be stated at all if it has a concrete anchor (a meaningful name, comment, config value, or external doc). With no anchor, the purpose is `unknown` and goes to the gap register — never a confident guess.

## 3. Confidence Tiers (4, mechanically testable)

Every business statement in every artifact MUST carry exactly one:

| Tier | Test | Typical use |
|---|---|---|
| `confirmed` | Restates deterministic, citation-verified behavior with no interpretive leap. | Endpoints, fields, validations, state transitions. |
| `doc-asserted` | Supported only by a comment/README/docstring, not by behavior. Comments can lie → ranks below confirmed. | Self-described purpose. |
| `inferred` | Behaviorally supported but requires a naming/intent judgment a reasonable person could dispute. Must cite evidence and state the inference. | Capability names, process narratives, business purpose. |
| `unknown` | No code evidence. Must NOT appear as a business statement — gap register only. | Dead code, external systems, undetermined intent. |

Default when unsure = `inferred`. Never round up.

## 4. Evidence — the Citation Format (every claim, every artifact)

Each business claim carries a machine-parseable evidence envelope. Anchor to symbols, not line numbers (line numbers rot on the first edit):

```
[[evidence
  repo: <repo-id>
  commit: <sha-the-run-was-extracted-against>
  path: <relative/path>
  symbol: <module.Class.method | function | route | model.field>
  lines: <hint-only, e.g. 40-47>
  hash: <content hash of the cited symbol>
  claim-type: what | why
  confidence: confirmed | doc-asserted | inferred | unknown
  derivation: <one line: how this was concluded>
]]
```

`claim-type` is mechanically enforced: a `why` claim is auto-capped at `inferred` — any `claim-type: why` + `confidence: confirmed` is a blocker (no prose judgment needed).

In `wiki/**` a claim carries the full envelope. In `business-docs/**` it carries only a reference (`[[evidence: CLAIM-<id>]]`) so the narrative stays code-free (§10); the publisher resolves the reference into the "Show me why" control on the site and into `traceability-matrix.md`. A claim with no envelope/reference is a defect, not a finding.

## 5. Stable Node IDs (anti-drift)

`codebase-cartographer` issues stable IDs and every downstream agent binds by ID, never by re-typed name (this prevents multiple agents naming the same concept multiple ways):

`CMP-*` component/module · `ENT-*` domain entity · `STORE-*` data store · `INT-*` external integration · `JOB-*` scheduled/batch job · `RULE-*` business rule · `CAP-*` capability · `PROC-*` process · `TERM-*` glossary term.

## 6. Output Layout (generated output)

The loop writes only under a top-level `business-use-case/<repo>/` folder (generated output; gitignored). It never modifies the analyzed repo's code. `<repo>` is the id from the configured repo allow-list.

```
business-use-case/<repo>/
  _index.md                     # top index (owned by scope-intake; finalized by publisher)
  checkpoint.json                # durable run state (see §8)
  wiki/                          # the reverse-engineered UNDERSTANDING (evidence-dense)
    system-map.md                # cartographer — components/stores/jobs/integrations + node registry
    glossary.md                  # glossary-curator — authoritative terms (data attributes as sub-layer)
    business-rules-catalog.md    # rule-miner — plain decision tables, each source-cited
    capability-map.md            # capability-mapper — functional decomposition
    process-flows.md             # capability-mapper — swimlane flows + Given/When/Then journeys
    batch-calendar.md            # capability-mapper — processing-cycle timeline (if any)
    outputs-inventory.md         # reports/files/screens the system produces
    integrations.md              # external touchpoints in business terms
    where-used.md                # impact / where-used cross-reference
  business-docs/                 # the AUDIENCE-TAILORED final deliverable (plain language)
    executive-one-pager.md
    system-overview.md
    (curated narrative pages assembled from the approved wiki)
  evidence/                      # facts-appendix → cartographer; the rest → publisher (derived)
    facts-appendix.md            # cartographer — the hard inventory (coverage denominator)
    traceability-matrix.md       # publisher — every claim ↔ its source (derived)
    gap-register.md              # publisher — everything undetermined / needs-SME (derived)
    coverage-report.md           # publisher — coverage % + confidence mix + readability (derived)
    review-queue-<gate>.md       # publisher — ranked 'needs your decision' queue per gate
  site/                          # BA-facing static site (publisher renders)
    index.html
```

**Ownership (single-writer per file):** `_index.md` → scope-intake scaffolds, publisher finalizes. `wiki/system-map.md` → cartographer. `wiki/glossary.md` → glossary-curator. `wiki/business-rules-catalog.md` → rule-miner. `wiki/{capability-map,process-flows,batch-calendar,outputs-inventory,integrations,where-used}.md` → capability-mapper. `business-docs/**` → business-doc-writer (no code access — transforms only approved wiki content). `evidence/facts-appendix.md` → codebase-cartographer (the raw coverage inventory, produced in Stage 1 and only read by the publisher — the one carve-out from the rule below). `evidence/**` (traceability-matrix, gap-register, coverage-report, review-queue-\<gate\>) and `site/**` → business-doc-publisher (derived; no other agent writes them).

## 7. Fidelity — Standards-Informed, Not Standards-Notated

Keep the rigor of the standards; drop the intimidating notation for this audience.
- Business rules → plain decision tables (spreadsheet look): condition columns + outcome columns in business language. No formal decision-notation expressions, hit-policy letters, or decision-requirement diagrams.
- Processes → simple swimlanes / numbered steps: one lane per business role, ≤7 shapes, plain labels. No formal process-notation gateways/event symbols/pools.
- Rules text → constrained plain English: "A payment must be under the daily limit unless it is pre-authorized." Term-anchored, atomic, testable — but no formal rule-notation markup.

## 8. Idempotency, Drift & Checkpoints

- **Content-based idempotency.** Pin the extraction commit SHA in `checkpoint.json`. On re-run, diff current SHA vs. pinned; any artifact whose evidence touches a changed symbol has its artifact-status set to `stale` (staleness is a status, never a 5th confidence tier), and only stale items + dependents are re-processed. Untouched human approvals are preserved. Surface the delta at a Drift Gate — the BA re-approves only what changed, and the loop resumes at the earliest stale stage.
- **Deterministic slug→path.** Re-runs overwrite a page at its path; update `_index.md` in place; prune pages whose source no longer exists.
- `checkpoint.json` MUST hold: repo id + remote + branch + pinned SHA; the analyst's focus/scope-selection (Stage 1.5); stage + sub-stage; per-artifact status `{not-started|drafted|critiqued|approved|stale}`; per-artifact critic-iteration count; per-item human-decision log; the approved glossary snapshot (frozen at Gate 2a; the required input to Stage 2b); coverage metrics; gap-register state; per-evidence content hashes.
- **Checkpoint writers:** `business-scope-intake` writes checkpoint #0 only. Thereafter the loop orchestrator (the skill) updates it at each stage/gate, and writes the approved glossary snapshot when Gate 2a is approved. No worker other than intake writes `checkpoint.json`.

## 9. Coverage & Honesty (deterministic denominator)

Two distinct, named metrics (never conflate them):
- `readability-coverage` (gates Gate 1) = readable files ÷ total files in scope. Floor = 60%; below it Gate 1 escalates to the dev team (the code is too opaque to document honestly).
- `documentation-coverage` (gates publish) = documented items ÷ parser-discovered items (from `facts-appendix.md`). Floor = 80% of in-scope items, unless the gap is explicitly accepted at Gate 3.
- For rules, report "% of rule-candidate sites triaged," never "% of business rules" (that number is unknowable).
- The gap register is auto-populated deterministically: every untriaged candidate, every stale/unresolvable citation, every data store with unknown attributes, every dynamic-dispatch edge the call graph could not resolve, every inferred purpose. It must never be optimistically empty.
- Publish the confidence mix ("X% confirmed / Y% inferred / Z% doc-asserted") next to coverage so high coverage of low-confidence content is visible.
- **Fail-closed:** an unverifiable citation is flagged, never silently passed. Zero-rules hard-stop: if rule-candidate-sites > 0 and rules-published == 0, stop for review. Exception: a repo whose `audience_fit` is low (developer tooling) expects few/no business rules — there the hard-stop relaxes to a warning and the deliverable opens with a thin-optics honesty banner (§10).

## 10. Audience & Tone Rules (enforced by writer + business-review-critic)

- **Glossary-first.** Define a term before using it, or link it.
- **No code in the narrative.** No identifiers, no API/endpoint/class/method/schema/null/boolean/payload/async/exception in business pages. Code lives only in the evidence appendix behind "Show me why."
- **"So-what" is mandatory.** Every section states the business impact, not the mechanism ("When a customer misses a payment, the account is flagged for review" — not "the batch job sets status=DLQ").
- **Reading level ≤ Grade 9** — computed deterministically by `business-doc-publisher`, not eyeballed; a page above Grade 10 fails closed at Gate 3. The code-blind `business-review-critic` judges comprehension, not the score.
- **Jargon lint** (positive test, run by the publisher): flag a fixed denylist (API/endpoint/class/method/schema/null/boolean/payload/async/exception, and formal rule/process-notation terms) and any code-shaped token (`snake_case`, `camelCase`, `CamelCase`, `name()`) and any noun not defined in the glossary and not everyday English. Any hit in `business-docs/**` fails closed.
- **Legacy-system traps:** never read technical status codes as business states, scheduler wiring as business logic, or raw field names as business terms without an SME flag — mark these inferred. Exception: in a run/workflow-orchestration domain the run/job status machine IS the business domain — its transitions are legitimate rule candidates, but every why stays inferred.

## 11. Human Gates (supervised)

`GATE 1 Approve Scope & Map` → `GATE 2a Approve Vocabulary` → `GATE 2b Approve Business Logic` → `GATE 3 Approve & Publish`; re-runs pass a `GATE 0.5 Drift review`.

Every gate: the relevant critic must pass first (only blocker/major stop the gate). The human then reviews the exception-driven queue (`evidence/review-queue-<gate>.md`) — a one-screen plain-language summary plus a ranked list of low-confidence × high-impact + gaps; confirmed-by-code items auto-pass with spot-check. Contested items have an escape hatch (accept-as-inferred | drop | escalate-to-named-SME) and never block the gate indefinitely (human↔worker cap = 3 round-trips per item).

**Severity rubric** (all critics use this):
| Severity | Definition | Effect |
|---|---|---|
| blocker | Unverifiable/broken citation; a WHY marked confirmed; an invented node/rule; a business-docs claim with no approved ancestor; zero-rules hard-stop tripped. | Gate cannot pass. |
| major | Technical noise sold as a business rule; mislabeled confidence; jargon/readability failure; missing major component; optimistic coverage. | Gate cannot pass. |
| minor | Wording, ordering, non-load-bearing polish. | Backlog; gate may pass. |

**Writer-fidelity gate** (before Gate 3): `findings-critic` (not the code-blind reviewer) diffs every `business-docs/**` claim against its approved `wiki/**` ancestor by node ID + envelope hash; any business-docs claim without an identical approved ancestor, or with an upgraded confidence badge, is a blocker.

**Fresh-context invocation:** critics are launched with only `{artifact path, repo, pinned SHA}` — never the producing worker's chat text or reasoning. A critic re-resolves 100% of citations (sampling is allowed only for the deeper semantic re-read).

## 12. Anti-Patterns (forbidden across the loop)

- Emitting a business claim with no evidence envelope.
- Marking any WHY/purpose claim as confirmed.
- A worker writing another worker's file, or writing outside `business-use-case/<repo>/`.
- Modifying the analyzed repo's code.
- Presenting an empty gap register as "complete."
- Using formal decision/process-notation markup, code identifiers, or jargon in the business-docs narrative.
- A critic reasoning from the producer's chat context instead of a fresh read of the artifact + code.
