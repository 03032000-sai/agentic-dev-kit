---
name: frontmatter-indexer
description: Audit and fix YAML frontmatter on design/implementation wiki pages so metadata reflects current page content. Use when reviewing wiki pages, updating frontmatter after edits, validating abstracts match body, ensuring tags cover key topics, checking stage/confidence accuracy.
---

# Frontmatter Indexer

Ensures YAML frontmatter on wiki pages (see the `system-design` / `implementation-design` frontmatter schemas) accurately reflects the current state of the page body. Detects drift between metadata claims and actual content.

## When to Use
- After editing wiki page body content — to sync frontmatter.
- During review — to validate all pages in a directory have accurate metadata.
- When an abstract feels stale or tags are missing key concepts from the body.
- When `stage` or `confidence` no longer reflects the page's maturity.

## Procedure

**Step 1 — Identify target pages.** If a specific file path is provided, use that. If a directory is provided, list all `.md` files in it (excluding `_index.md`). If no argument is given, infer the relevant wiki location from the invoking agent's current context.

**Step 2 — Read the full page.** For each target page, read the entire file — both frontmatter and body.

**Step 3 — Audit each frontmatter field against the body content:**
| Field | Audit Check |
|---|---|
| `title` | Does it match the primary `#` heading? Concise and descriptive. |
| `abstract` | Does the 1-2 sentence summary accurately capture the page's current scope and conclusions? Flag if the body has evolved beyond what the abstract describes. |
| `stage` | `seed` = initial exploration, `draft` = structure in place with open questions, `refined` = reviewed and validated, `stable` = accepted baseline. Does current body maturity match? |
| `confidence` | `hypothesis` = speculative/untested, `emerging` = directionally sound but incomplete, `established` = validated and agreed. Does body evidence support the claimed confidence? |
| `domain` | Does it correctly identify the bounded context or layer this page belongs to? |
| `type` | Options: `concept`, `pattern`, `decision`, `flow`, `index`, `blueprint`, `integration`. Is it accurate? |
| `depends-on` | Are all pages referenced in the body listed? Any listed dependency no longer referenced? |
| `tags` | Extract key nouns, patterns, and domain terms from the body. Are they represented? Flag missing high-signal terms and stale tags that no longer appear in the body. |
| `complexity` | Does low/medium/high match the actual depth and breadth of the page? |
| `created` / `updated` | Does `updated` reflect the last meaningful edit? Flag if content appears newer than the date. |

**Step 4 — Produce an audit report** per page:
```markdown
## [filename]

**Status**: ✅ Current | ⚠️ Drift detected | ❌ Stale

### Issues
- [field]: [what's wrong] → [suggested fix]

### Suggested Frontmatter (only if changes are needed)
```

**Step 5 — Apply fixes.** After producing the report, automatically apply the corrected frontmatter. Show what changed (before → after for each field). Only modify the YAML frontmatter block — never alter the page body. If the user explicitly asks for report-only mode ("just audit," "dry run"), skip this step and output the report only.

## Decision Rules
- **Abstract drift:** if the body covers topics not mentioned in the abstract, or the abstract promises content the body doesn't deliver → update the abstract.
- **Stage promotion:** if a page marked `seed` has clear structure, resolved decisions, and no open questions → promote to `draft` or `refined`.
- **Confidence promotion:** if speculative content now has supporting evidence or agreement markers → promote confidence.
- **Tag inflation:** keep tags to 5-12 high-signal terms; remove generic terms (`design`, `system`) unless the page is specifically about those meta-concepts.
- **`depends-on` hygiene:** only list pages that provide prerequisite context; remove transitive dependencies (if A depends-on B depends-on C, A should not list C unless it directly references C).

## Scope
This skill operates on design/implementation wiki pages (e.g. `docs/design/**/*.md`, `docs/implementation/**/*.md`, or their multi-repo equivalents under `repos/<repo>/docs/{design,implementation}/`). It does NOT touch `_index.md` files (those are navigation, not content pages).
