# lippertzpy

Eine kleine Python-Bibliothek für die Jifeline Partner API und lokales Logging.

## Voraussetzungen

- Python 3.10 oder neuer
- Zugangsdaten für die Jifeline Partner API

## Installation

Direkt aus dem Projektordner:

```powershell
py -m pip install .
```

Für die Entwicklung:

```powershell
py -m pip install -e .
```

## Konfiguration

Kopiere `.env.example` nach `.env` und trage deine Zugangsdaten ein:

```dotenv
client_id=your_client_id
client_secret=your_client_secret
```

Die `.env`-Datei wird von Git ignoriert und darf nicht veröffentlicht werden.
Sie wird im Verzeichnis des gestarteten Python-Skripts gesucht.

## Verwendung

```python
from lippertzpy import get, post, write_log

write_log("API client gestartet")
result = get("endpoint")
```

Unterstützte API-Funktionen sind `get`, `post`, `put` und `delete`.
`post` und `put` erwarten die zu sendenden Daten als zweites Argument.

Die Protokolldateien werden automatisch im Ordner `log` neben dem gestarteten
Python-Skript gespeichert.

## Tests

```powershell
py -m unittest discover -s tests
```

Bei Pushes und Pull Requests führt GitHub Actions die Tests automatisch aus.
