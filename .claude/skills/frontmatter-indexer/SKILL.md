---
name: frontmatter-indexer
description: Build deterministic indexes over Markdown agent, skill, prompt, and instruction frontmatter for discovery, routing, and validation.
---

# Frontmatter Indexer

## Mission
Create a machine-readable catalog of repository-native AI assets without parsing their full bodies at runtime.

## Inputs
Scan configured Markdown locations such as:
- `.github/agents/*.agent.md`;
- `.github/prompts/*.prompt.md`;
- `.github/instructions/*.instructions.md`;
- `.agents/skills/*/SKILL.md`;
- `.claude/agents/*.md`;
- `.claude/skills/*/SKILL.md`.

## Extract
At minimum:
- relative path;
- asset type;
- name;
- description;
- optional apply/include patterns;
- optional tools/capabilities metadata;
- checksum/content SHA.

## Rules
- YAML frontmatter must be syntactically valid;
- duplicate canonical names are errors unless an alias is explicitly supported;
- missing required name/description is an error;
- index ordering must be deterministic;
- generated indexes must never contain secrets;
- body text is not a substitute for missing routing metadata.

## Output
Write a deterministic JSON/Markdown index suitable for discovery and CI diffing.

## Validation
Run twice with unchanged inputs and require identical output. Add a negative fixture for malformed frontmatter and duplicate names.
