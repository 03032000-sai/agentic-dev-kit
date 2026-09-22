# Agentic Asset Index

The repository includes a deterministic frontmatter indexer for agentic assets.

## Build

~~~bash
python3 scripts/build_asset_index.py --output .agents/asset-index.json
~~~

or:

~~~bash
make asset-index
~~~

The default runtime index path is gitignored. CI builds an index in a temporary path to verify that all supported frontmatter can be parsed.

## Indexed asset classes

- GitHub Copilot agents
- GitHub Copilot prompt files
- GitHub Copilot path instructions
- canonical skills under .agents/skills
- Claude agents
- Claude skill mirrors

Each entry contains a stable type, name, repository-relative path, SHA-256 content digest, and routing metadata such as description/applyTo when present.

## Determinism

The index intentionally contains no timestamp. With unchanged repository content, repeated runs produce byte-for-byte identical JSON.

The index is a discovery accelerator, not an authority override: AGENTS.md and the canonical skill/agent files remain authoritative.
