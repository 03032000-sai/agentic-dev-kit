---
name: uv-python
description: Use uv for fast, reproducible Python dependency and environment workflows while respecting established repository conventions.
---

# uv Python

## Use when
The repository already uses uv, requests migration to uv, or has no established Python package workflow and the user accepts uv as the default.

## Principles
- keep `pyproject.toml` authoritative;
- commit the uv lockfile when reproducibility is required;
- use `uv sync` for environment realization;
- use `uv run` for repository commands where appropriate;
- separate runtime, dev, test, and optional dependency groups deliberately;
- do not manually edit resolved lock content;
- prefer explicit Python-version constraints.

## Migration
When converting from pip/requirements/Poetry/etc., preserve current dependency intent and test the resulting environment before deleting legacy files.

## Conflict rule
An established repository-specific workflow may override uv. Do not churn tooling merely because uv is available.

## Validation
Fresh environment → sync → lint/type/test/build as applicable.
