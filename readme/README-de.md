# lippertzpy

Eine kleine Python-Bibliothek für die Jifeline Partner API und lokales Logging.

> Vereinfachte API-Anfragen, zentrale Zugangsdaten und automatische Logdateien direkt neben deinen Scripts.

## Language

- [README English](README.md)

## Funktionen

- Einfacher Zugriff auf die Jifeline Partner API
- Hilfsfunktionen für `get`, `post`, `put` und `delete`
- Lokales Logging für Debugging und Überwachung
- Ideal für Skripte und kleine Automationen

## Voraussetzungen

- Python 3.10 oder neuer
- Gültige Zugangsdaten für die Jifeline Partner API

## Installation

Lade den Quellcode herunter und installiere die Bibliothek mit:

```bash
py -m pip install .
```

Oder direkt aus GitHub:

```bash
py -m pip install git+https://github.com/R0g3rT/lippertzPy.git
cd lippertzpy
python -m pip install -
```

Aktualisieren:

```bash
python -m pip install --upgrade lippertzpy
```

## Deinstallation:

```bash
py -m pip uninstall lippertzpy
```

## Konfiguration

Erstelle eine `.env`-Datei in deinem Projektordner oder neben deinem Script und trage deine Zugangsdaten ein:

```dotenv
client_id=your_client_id
client_secret=your_client_secret
```

Wenn vorhanden, kannst du auch die Beispiel-Datei kopieren.

## Schnellstart

```python
from lippertzpy import get, post, write_log

write_log("API client gestartet", "INFO")
write_log("Wichtige Warnung", "WARNING")
write_log("Ein Fehler ist aufgetreten", "ERROR")
result = get("endpoint")
result = post("endpoint", {"data": data})
```

## Unterstützte API-Methoden

Die Bibliothek unterstützt folgende HTTP-Methoden:

- `get`
- `post`
- `put`
- `delete`

Das zweite Argument von `post` und `put` enthält die zu sendenden Daten.

## Logging

- `INFO`
- `WARNING`
- `ERROR`
- `CRITICAL`

Die Protokolldateien werden automatisch im Ordner `log` neben dem gestarteten Python-Skript gespeichert.
