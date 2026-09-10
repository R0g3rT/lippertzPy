# lippertzpy

Python helpers for the Jifeline Partner API and local logging.

## Installation

After publication on PyPI:

```bash
python -m pip install lippertzpy
```

Upgrade to the latest published version:

```bash
python -m pip install --upgrade lippertzpy
```

Installation directly from GitHub remains possible:

```bash
python -m pip install git+https://github.com/R0g3rT/lippertzPy.git
```

For local development:

```bash
python -m pip install -e .
```

## Usage

```python
from lippertzpy import get, post, write_log

write_log("API client gestartet")
result = get("endpoint")
result = post("endpoint", {"data": data})
```

The package exports the Jifeline API helpers `get`, `post`, `put`, `delete` and `get_access_token`, as well as the logging helpers `setup_logging` and `write_log`.

## Configuration

Copy `.env.example` to `your-script-folder\.env` or create a file `.env` in your directory and enter your credentials.

Do not commit your real `.env` file or credentials to GitHub.

## Documentation

- [README Deutsch](readme/README-de.md)
- [README English](readme/README-en.md)

## Releases

The package is prepared for publishing to PyPI through GitHub Actions and PyPI Trusted Publishing. A published GitHub Release triggers the PyPI publishing workflow.

Before creating a new release, increase the version in `pyproject.toml`, for example from `0.1.2` to `0.1.3`.
