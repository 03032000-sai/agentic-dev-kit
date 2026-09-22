# agentic-dev-kit

A repository-native, local chat agent framework for disciplined software engineering with GitHub Copilot, Claude Code, and OpenAI Codex.

There is no Python runtime or orchestration server in v0.2. The repository itself is the agent system: custom agents, reusable skills, prompt entry points, instructions, contracts, and engineering loops invoked directly from chat.

> Non-deterministic AI reasoning should be surrounded by deterministic engineering controls.

## Specialist agents

### Core
- Repository Analyst
- System Designer
- Implementation Designer
- Implementer
- Independent Critic
- Local Operator
- Clean-Repo Operator
- Git Manager
- Traceability Analyst
- Docs-Code Aligner
- Security Reviewer

### Business documentation
- Business Scope Intake
- Codebase Cartographer
- Domain Glossary Curator
- Business Rule Miner
- Process Capability Mapper
- Business Doc Writer
- Business Doc Publisher

### Multi-repo
- Multi-Repo Bootstrapper
- Cross-Repo Discovery

## Engineering loops

- Incremental Design / Build
- Feature Development
- Bug Fix
- Brownfield Bootstrap
- Reverse-Engineer Design
- Docs ↔ Code Alignment
- Knowledge Discovery
- Safe Refactor
- Security Remediation
- Release Readiness
- Business Documentation
- Multi-Repo Bootstrap

## Additional skills

Narrow, reusable skills invoked by the loops above or directly when relevant: `semgrep-sast-rules`, `trivy-sca-scanning`, `mitre-attack-mapping`, `transitive-dependency-remediation`, `vuln-enrichment-prioritization`, `docker-podman-optimizer`, `uv-python`, `oauth2-pkce-integration`, `private-package-registry-config`, `frontmatter-indexer`, `skill-scaffolding`.

## How to invoke

### GitHub Copilot

Select a custom role from the Agent picker. For complete workflows, run a prompt file from `.github/prompts/`, such as `incremental-design-build`, `bugfix`, or `brownfield-bootstrap`.

Copilot can also load matching skills from `.agents/skills/`.

### Claude Code

Claude Code reads `CLAUDE.md`.

Use `/agents` to inspect custom agents. Skills under `.claude/skills/` can be called from chat, for example:

```text
/incremental-design-build Add rate limiting to this API
/bugfix Fix duplicate event processing
/knowledge-discovery Explain authentication in this repo
```

### OpenAI Codex

Codex reads `AGENTS.md` automatically. Repository skills under `.agents/skills/` can be invoked explicitly:

```text
$incremental-design-build Add rate limiting to this API
$bugfix Fix duplicate event processing
$knowledge-discovery Explain authentication in this repo
```

## Default governed loop

```text
Requirement
  ↓
Discovery
  ↓
System Design
  ↓
Gate A / Critic
  ↓
Implementation Design
  ↓
Gate B / Critic
  ↓
Implementation
  ↓
Local Validation
  ↓
Clean Validation
  ↓
Gate C / Critic
  ↓
Human / Git Completion
```

## Clean-room notice

This is an original public portfolio project built from general software-engineering and agentic-system design principles. It contains no proprietary employer source code, prompts, internal URLs, credentials, schemas, security findings, or confidential documentation.
