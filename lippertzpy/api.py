"""Helpers for calling the Jifeline partner API."""

import os
import sys
import time
from pathlib import Path
from typing import Any

import requests
from dotenv import load_dotenv

API_URL = "https://partner-api-001.prd.jifeline.cloud/v2/"
TOKEN_URL = "https://jifeline-user-pool-prd.auth.eu-central-1.amazoncognito.com/oauth2/token"

_session = requests.Session()
_token: str | None = None
_token_expires = 0.0


def get_access_token() -> str:
    """Request an OAuth access token and reuse it until shortly before it expires."""
    global _token, _token_expires
    if _token and time.time() < _token_expires:
        return _token

    load_dotenv(Path(sys.argv[0]).resolve().parent / ".env", override=False)
    client_id = os.getenv("client_id")
    client_secret = os.getenv("client_secret")
    if not client_id or not client_secret:
        raise RuntimeError("client_id oder client_secret fehlt in der .env-Datei.")

    response = _session.post(
        TOKEN_URL,
        data={
            "grant_type": "client_credentials",
            "client_id": client_id,
            "client_secret": client_secret,
        },
        timeout=30,
    )
    response.raise_for_status()
    payload = response.json()
    _token = payload["access_token"]
    _token_expires = time.time() + payload.get("expires_in", 3600) - 60
    return _token


def _request(method: str, endpoint: str, data: Any = None) -> Any:
    response = _session.request(
        method,
        API_URL + endpoint.lstrip("/"),
        json=data,
        headers={"Authorization": f"Bearer {get_access_token()}"},
        timeout=30,
    )
    if not response.ok:
        # Antworttext mitgeben, sonst geht die Fehlerursache der API verloren
        raise requests.HTTPError(
            f"{response.status_code} {method} {endpoint}: {response.text[:500]}",
            response=response,
        )
    return response.json() if response.content else {}


def get(endpoint: str) -> Any:
    return _request("GET", endpoint)


def post(endpoint: str, data: Any) -> Any:
    return _request("POST", endpoint, data)


def put(endpoint: str, data: Any) -> Any:
    return _request("PUT", endpoint, data)


def delete(endpoint: str) -> Any:
    return _request("DELETE", endpoint)
