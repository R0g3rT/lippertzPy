# lippertzpy

A lightweight Python library for the Jifeline Partner API and local logging.

> Simplify API requests, keep your authentication in one place, and automatically write log files next to your scripts.

## Language

- [README German](README-de.md)

## Features

- Easy access to the Jifeline Partner API
- Helpers for `get`, `post`, `put`, and `delete`
- OAuth token is cached and reused until shortly before it expires
- API error messages are included in the raised exception
- Local logging via [liplog](https://github.com/R0g3rT/liplog)

## Requirements

- Python 3.10 or newer
- Valid credentials for the Jifeline Partner API

## Installation

Install from PyPI:

```bash
python -m pip install lippertzpy
```

Install directly from GitHub:

```bash
python -m pip install git+https://github.com/R0g3rT/lippertzPy.git
```

Update:

```bash
python -m pip install --upgrade lippertzpy
```

Uninstall:

```bash
python -m pip uninstall lippertzpy
```

## Configuration

Create a `.env` file in the same folder as the Python script you start and add your credentials:

```dotenv
client_id=your_client_id
client_secret=your_client_secret
```

Alternatively, set `client_id` and `client_secret` as environment variables. Existing environment variables take precedence over the `.env` file.

## Quick start

```python
from lippertzpy import get, post, write_log

write_log("API client started", "RUN")

ticket = get("tickets/tickets/123")
result = post("endpoint", {"key": "value"})

write_log("Done", "SUCCESS")
```

## Supported API methods

- `get(endpoint)`
- `post(endpoint, data)`
- `put(endpoint, data)`
- `delete(endpoint)`

`data` is sent as JSON. Empty responses (e.g. `204 No Content`) return `{}`.
On HTTP errors a `requests.HTTPError` is raised that contains the status code and the response text of the API.

## Logging

`write_log` and `setup_logging` come from [liplog](https://github.com/R0g3rT/liplog).

Supported levels: `DEBUG`, `RUN`, `INFO`, `SUCCESS`, `WARNING`, `ERROR`, `CRITICAL`. An unknown level raises a `ValueError`.

Log files are stored in `logs/<script>/` next to the Python script that was started. The folder is created on the first log entry.

## Changes in 0.3.0

- Requires `liplog>=0.3.0`: log files are stored in `logs/<script>/`, `DEBUG` is supported, console output goes to stdout

## Changes in 0.2.0

- Logging now uses `liplog`: the log folder is `logs` (previously `log`)
- `write_log(message, level="INFO")`: the `retries` and `delay_ms` parameters were removed
- Requires Python 3.10 or newer
