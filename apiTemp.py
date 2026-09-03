"""Compatibility wrapper for the installable :mod:`lippertzpy` package."""

from lippertzpy.api import delete, get, get_access_token, post, put
from lippertzpy.logging import write_log

__all__ = ["delete", "get", "get_access_token", "post", "put", "write_log"]

