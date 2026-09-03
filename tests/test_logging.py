import os
from pathlib import Path
import sys
import unittest
from unittest.mock import patch


class LoggingTests(unittest.TestCase):
    def test_log_directory_is_created_next_to_script(self) -> None:
        project_root = Path(__file__).resolve().parents[1]
        script = project_root / "sample" / "example.py"

        with patch.dict(os.environ, {"CHECK_SEPA_COMBINED_LOG": "1"}):
            from lippertzpy import logging as package_logging

        with (
            patch.dict(os.environ, {}, clear=True),
            patch.object(sys, "argv", [str(script)]),
            patch.object(Path, "mkdir") as mkdir,
            patch.object(package_logging.logging, "FileHandler"),
            patch.object(package_logging.logging, "StreamHandler"),
            patch.object(package_logging.logging, "basicConfig"),
        ):
            reported_path = Path(package_logging.setup_logging("example"))

        self.assertEqual(reported_path.parent, script.parent / "log")
        self.assertTrue(reported_path.name.startswith("example-"))
        self.assertEqual(reported_path.suffix, ".log")
        mkdir.assert_called_once_with(exist_ok=True)


if __name__ == "__main__":
    unittest.main()
