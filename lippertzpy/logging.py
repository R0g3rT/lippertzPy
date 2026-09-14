import logging
import sys
from datetime import datetime
from pathlib import Path


class _DisplayLevelFormatter(logging.Formatter):
    """Use the custom display level in the formatted log message."""

    def format(self, record: logging.LogRecord) -> str:
        display_level = getattr(record, "display_level", None)
        if display_level is None:
            return super().format(record)

        original_level = record.levelname
        record.levelname = display_level
        try:
            return super().format(record)
        finally:
            record.levelname = original_level


class _ColorFormatter(_DisplayLevelFormatter):
    """Add ANSI colors to console messages without changing file logs."""

    _COLORS = {
        "ERROR": "91", # Red
        "WARNING": "93", # Yellow
        "SUCCESS": "92", # Green
        "RUN": "94", # Blue
        "DEBUG": "90", # Gray
        "INFO": "0", # White
        "CRITICAL": "95", # Magenta
    }

    def format(self, record: logging.LogRecord) -> str:
        color = self._COLORS.get(getattr(record, "display_level", record.levelname))
        message = super().format(record)
        return f"\033[{color}m{message}\033[0m" if color else message


def setup_logging(log_name: str | None = None) -> str | None:
    """Configure console and file logging and return the log file path."""
    script_dir = Path(sys.argv[0]).resolve().parent
    log_dir = script_dir / "log"
    log_dir.mkdir(exist_ok=True)
    script_name = log_name or Path(sys.argv[0]).stem or "lippertzpy"
    safe_name = "".join(
        character if character.isalnum() or character in "-_" else "_"
        for character in script_name
    )
    log_file = log_dir / f"{safe_name}-{datetime.now():%Y-%m-%d_%H-%M}.log"

    log_format = "[%(asctime)s] [%(levelname)s] %(message)s"
    date_format = "%Y-%m-%d %H:%M:%S"
    file_handler = logging.FileHandler(log_file, encoding="utf-8")
    file_handler.setFormatter(_DisplayLevelFormatter(log_format, datefmt=date_format))
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(_ColorFormatter(log_format, datefmt=date_format))
    logging.basicConfig(level=logging.INFO, handlers=[file_handler, console_handler])
    return str(log_file)


_log_file = setup_logging()


def write_log(message: str, level, retries: int = 6, delay_ms: int = 150) -> None:
    """Write a message to the configured log and console."""
    del retries, delay_ms
    if _log_file is not None:
        normalized_level = level.upper()
        logging.log(
            getattr(logging, normalized_level, logging.INFO),
            message,
            extra={"display_level": normalized_level},
        )
