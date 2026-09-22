---
name: uv-python
description: Use uv for all Python package and virtual environment management. Use when creating a new Python project, adding/removing dependencies, setting up a venv, running Python scripts or tests, installing packages, managing pyproject.toml, or running any pip/venv/virtualenv command. Replaces pip, pip-tools, virtualenv, and venv for all operations.
---

# uv Python Package & Environment Management

## When to Use
Use this skill for all Python project operations: creating a new virtual environment; installing, upgrading, or removing packages; running Python scripts, tests, or tools; managing `pyproject.toml` dependencies; syncing dependencies from lock files; any task that would traditionally use `pip`, `pip-tools`, `virtualenv`, or `python -m venv`.

## Core Principles
- Never use `pip install` — always use `uv add` or `uv pip install`.
- Never use `python -m venv` — always use `uv venv`.
- Never use `pip-compile` — always use `uv lock`.
- Use `uv run` to execute scripts/tools within the project environment without activating manually.

## Procedures

**Create a new virtual environment**
```bash
uv venv                        # creates .venv in current directory
uv venv --python 3.12          # pin to a specific Python version
```

**Install / add dependencies**
```bash
uv add <package>                       # runtime dependency, updates pyproject.toml + lock
uv add "fastapi>=0.110"
uv add --dev pytest ruff mypy          # dev/test dependency
uv sync                                # install all dependencies from pyproject.toml
uv sync --extra dev                    # include optional groups
```

**Remove a dependency**
```bash
uv remove <package>
```

**Run scripts and tools**
```bash
uv run python script.py
uv run pytest tests/ -v
uv run mypy src/
uvx ruff check .    # run a one-off tool without adding it as a dependency
uvx black .
```

**Lock and reproduce environments**
```bash
uv lock               # generate/update uv.lock
uv sync               # install exactly what's in uv.lock
```

**Upgrade packages**
```bash
uv add --upgrade <package>     # upgrade a specific package
uv lock --upgrade              # upgrade all packages in lock file
uv sync                        # apply upgraded lock
```

**Editable / local package install**
```bash
uv pip install -e .    # equivalent to pip install -e .
# or declare via pyproject.toml and use uv sync
```

**Check installed packages**
```bash
uv pip list
uv pip show <package>
```

## `pyproject.toml` Conventions
```toml
[project]
name = "my-package"
version = "0.1.0"
requires-python = ">=3.11"
dependencies = [
    "fastapi>=0.110",
    "pydantic>=2.0",
]

[project.optional-dependencies]
dev = [
    "pytest>=8.0",
    "ruff",
    "mypy",
]

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"
```

## Decision Table: uv Equivalents
| Old command | uv equivalent |
|---|---|
| `pip install <pkg>` | `uv add <pkg>` |
| `pip install -r requirements.txt` | `uv pip install -r requirements.txt` |
| `pip install -e .` | `uv pip install -e .` |
| `pip uninstall <pkg>` | `uv remove <pkg>` |
| `pip list` | `uv pip list` |
| `python -m venv .venv` | `uv venv` |
| `pip-compile` | `uv lock` |
| `pip-sync` | `uv sync` |
| `python script.py` (in venv) | `uv run python script.py` |
| `pytest` (in venv) | `uv run pytest` |

## Notes
- `uv` is significantly faster than `pip` due to its Rust-based resolver.
- `uv.lock` is the lockfile — commit it to version control for reproducibility.
- If `uv` is not installed, bootstrap it with `curl -LsSf https://astral.sh/uv/install.sh | sh`.
- Prefer `uv sync` over manual activation + pip for CI/CD and scripted workflows.
