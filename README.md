# lippertzpy

A lightweight Python library for the Jifeline Partner API and local logging.

> Simplify API requests, keep your authentication in one place, and automatically write log files next to your scripts.

## Language

- [README German](/readme/README-de.md)

## Features

- Easy access to the Jifeline Partner API
- Helpers for `get`, `post`, `put`, and `delete`
- Local log writing for debugging and monitoring
- Ready for scripts and small automations

## Requirements

- Python 3.10 or newer
- Valid credentials for the Jifeline Partner API

## Installation

Download the source code and install it with:

```bash
py -m pip install .
```

Or install directly from GitHub:

```bash
py -m pip install git+https://github.com/R0g3rT/lippertzPy.git
cd lippertzpy
python -m pip install -
```

Update:

```bash
python -m pip install --upgrade lippertzpy
```


To uninstall:

```bash
py -m pip uninstall lippertzpy
```

## Configuration

Create a `.env` file in your project directory or next to your script and add your credentials:

```dotenv
client_id=your_client_id
client_secret=your_client_secret
```

You can also copy the example file if available in your project.

## Quick start

```python
from lippertzpy import get, post, write_log

write_log("API client started", "INFO")
write_log("Important warning", "WARNING")
write_log("An error occurred", "ERROR")
result = get("endpoint")
result = post("endpoint", {"data": data})
```

## Supported API methods

The library supports the following request methods:

- `get`
- `post`
- `put`
- `delete`

The second argument of `post` and `put` is the payload to send.

## Logging

- `INFO`
- `WARNING`
- `ERROR`
- `DEBUG`
- `CRITICAL`

Log files are automatically stored in a `log` folder next to the Python script that started the application.
