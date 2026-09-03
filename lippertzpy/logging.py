"""Logging helpers used by the library."""

import logging
import os
import sys
from datetime import datetime
from pathlib import Path


def setup_logging(log_name: str | None = None) -> str | None:
    """Configure console and file logging and return the log file path."""
    if os.environ.get("CHECK_SEPA_COMBINED_LOG") == "1":
        return None

    script_dir = Path(sys.argv[0]).resolve().parent
    log_dir = script_dir / "log"
    log_dir.mkdir(exist_ok=True)
    script_name = log_name or Path(sys.argv[0]).stem or "lippertzpy"
    safe_name = "".join(
        character if character.isalnum() or character in "-_" else "_"
        for character in script_name
    )
    log_file = log_dir / f"{safe_name}-{datetime.now():%Y-%m-%d_%H-%M}.log"

    logging.basicConfig(
        level=logging.INFO,
        format="[%(asctime)s] [%(levelname)s] %(message)s",
        handlers=[
            logging.FileHandler(log_file, encoding="utf-8"),
            logging.StreamHandler(),
        ],
    )
    return str(log_file)


_log_file = setup_logging()


def write_log(message: str, level: str = "INFO", retries: int = 6, delay_ms: int = 150) -> None:
    """Write a message to the configured log and console."""
    del retries, delay_ms
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] [{level}] {message}"
    if _log_file is not None:
        logging.log(getattr(logging, level.upper(), logging.INFO), message)

    if os.environ.get("CHECK_SEPA_COMBINED_LOG") == "1":
        script_name = os.environ.get("CHECK_SEPA_SCRIPT_NAME") or Path(sys.argv[0]).stem
        print(f"[{script_name}] {log_entry}", flush=True)
        return

    color = {"ERROR": "91", "WARNING": "93", "SUCCESS": "92", "RUN": "94"}.get(level.upper())
    output = f"[{timestamp}] {message}"
    print(f"\033[{color}m{output}\033[0m" if color else output)
