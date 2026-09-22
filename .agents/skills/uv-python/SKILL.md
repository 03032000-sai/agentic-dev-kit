---
name: uv-python
description: Manage Python dependencies and environments with uv instead of pip/venv/pip-tools.
---

# uv Python Tooling
Use `uv` for all Python dependency and environment management in this project: `uv venv` for environments, `uv add`/`uv remove` for dependencies, `uv sync` to install from the lockfile, `uv run` to execute in-environment. Commit the `uv.lock` file. Do not mix `pip install` into a `uv`-managed environment — it drifts the lockfile out of sync silently.
