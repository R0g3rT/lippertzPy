# lippertzpy

A small Python library for the Jifeline Partner API and local logging.

## Requirements

- Python 3.10 or newer
- Credentials for the Jifeline Partner API

## Installation

Download the code, then:

```powershell
py -m pip install .
```
or

```powershell
py -m pip install git+https://github.com/R0g3rT/lippertzPy.git
```

For development:

```powershell
py -m pip install -e .
```

To uninstall:

```powershell
py -m pip uninstall lippertzpy
```

## Configuration

Copy `.env.example` to `your-script-folder\.env` and fill in your credentials:

```dotenv
client_id=your_client_id
client_secret=your_client_secret
```

## Usage

```python
from lippertzpy import get, post, write_log

write_log("API client started")
result = get("endpoint")
result = post("endpoint", {"data": data})
```

Supported API functions are `get`, `post`, `put`, and `delete`.
`post` and `put` expect the data to send as the second argument.

Log files are automatically saved in the `log` folder next to the
Python script that was started.