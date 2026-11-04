# lippertzpy

Eine kleine Python-Bibliothek für die Jifeline Partner API und lokales Logging.

> Vereinfachte API-Anfragen, zentrale Zugangsdaten und automatische Logdateien direkt neben deinen Scripts.

## Sprache

- [README English](README.md)

## Funktionen

- Einfacher Zugriff auf die Jifeline Partner API
- Hilfsfunktionen für `get`, `post`, `put` und `delete`
- OAuth-Token wird zwischengespeichert und bis kurz vor Ablauf wiederverwendet
- Fehlermeldungen der API landen in der ausgelösten Exception
- Lokales Logging über [liplog](https://github.com/R0g3rT/liplog)

## Voraussetzungen

- Python 3.10 oder neuer
- Gültige Zugangsdaten für die Jifeline Partner API

## Installation

Über PyPI:

```bash
python -m pip install lippertzpy
```

Direkt aus GitHub:

```bash
python -m pip install git+https://github.com/R0g3rT/lippertzPy.git
```

Aktualisieren:

```bash
python -m pip install --upgrade lippertzpy
```

Deinstallieren:

```bash
python -m pip uninstall lippertzpy
```

## Konfiguration

Erstelle eine `.env`-Datei im selben Ordner wie das gestartete Python-Script und trage deine Zugangsdaten ein:

```dotenv
client_id=your_client_id
client_secret=your_client_secret
```

Alternativ kannst du `client_id` und `client_secret` als Umgebungsvariablen setzen. Vorhandene Umgebungsvariablen haben Vorrang vor der `.env`-Datei.

## Schnellstart

```python
from lippertzpy import get, post, write_log

write_log("API client gestartet", "RUN")

ticket = get("tickets/tickets/123")
result = post("endpoint", {"key": "value"})

write_log("Fertig", "SUCCESS")
```

## Unterstützte API-Methoden

- `get(endpoint)`
- `post(endpoint, data)`
- `put(endpoint, data)`
- `delete(endpoint)`

`data` wird als JSON gesendet. Leere Antworten (z. B. `204 No Content`) ergeben `{}`.
Bei HTTP-Fehlern wird ein `requests.HTTPError` mit Statuscode und Antworttext der API ausgelöst.

## Logging

`write_log` und `setup_logging` kommen aus [liplog](https://github.com/R0g3rT/liplog).

Unterstützte Level: `DEBUG`, `RUN`, `INFO`, `SUCCESS`, `WARNING`, `ERROR`, `CRITICAL`. Ein unbekanntes Level löst einen `ValueError` aus.

Die Logdateien landen in `logs/<script>/` neben dem gestarteten Python-Script. Der Ordner wird beim ersten Log-Eintrag angelegt.

## Änderungen in 0.3.0

- Benötigt `liplog>=0.3.0`: Logdateien liegen in `logs/<script>/`, `DEBUG` wird unterstützt, Konsolenausgabe geht nach stdout

## Änderungen in 0.2.0

- Logging läuft jetzt über `liplog`: der Log-Ordner heißt `logs` (vorher `log`)
- `write_log(message, level="INFO")`: die Parameter `retries` und `delay_ms` sind entfallen
- Benötigt Python 3.10 oder neuer
