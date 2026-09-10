# lippertzpy

Eine kleine Python-Bibliothek für die Jifeline Partner API und lokales Logging.

## Voraussetzungen

- Python 3.10 oder neuer
- Zugangsdaten für die Jifeline Partner API

## Installation

Download den Code und dann:

```powershell
pip install lippertzpy
```
or

```powershell
pip install git+https://github.com/R0g3rT/lippertzPy.git
```

```powershell
py -m pip uninstall lippertzpy
```

## Konfiguration

Kopiere `.env.example` nach `your-script-folder\.env` und trage deine Zugangsdaten ein:

```dotenv
client_id=your_client_id
client_secret=your_client_secret
```

## Verwendung

```python
from lippertzpy import get, post, write_log

write_log("API client gestartet")
result = get("endpoint")
result = post("endpoint", {"data": data})
```

Unterstützte API-Funktionen sind `get`, `post`, `put` und `delete`.
`post` und `put` erwarten die zu sendenden Daten als zweites Argument.

Die Protokolldateien werden automatisch im Ordner `log` neben dem gestarteten
Python-Skript gespeichert.