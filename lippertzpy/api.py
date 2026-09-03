"""Helpers for calling the Jifeline partner API."""

import os
from pathlib import Path
import sys

import requests
from dotenv import load_dotenv

API_URL = "https://partner-api-001.prd.jifeline.cloud/v2/"
TOKEN_URL = "https://jifeline-user-pool-prd.auth.eu-central-1.amazoncognito.com/oauth2/token"


def _load_environment() -> None:
    """Load .env from the directory containing the main script."""
    script_path = Path(sys.argv[0]).resolve()
    env_path = script_path.parent / ".env"
    load_dotenv(env_path, override=False)


def get_access_token() -> str:
    """Request an OAuth access token using client credentials."""
    _load_environment()
    client_id = os.getenv("client_id")
    client_secret = os.getenv("client_secret")
    if not client_id or not client_secret:
        raise RuntimeError("client_id oder client_secret fehlt in der .env-Datei.")

    response = requests.post(
        TOKEN_URL,
        data={
            "grant_type": "client_credentials",
            "client_id": client_id,
            "client_secret": client_secret,
        },
        headers={"Content-Type": "application/x-www-form-urlencoded"},
        timeout=30,
    )
    response.raise_for_status()
    return response.json()["access_token"]


def _headers() -> dict[str, str]:
    return {
        "Authorization": f"Bearer {get_access_token()}",
        "Content-Type": "application/json",
    }


def post(endpoint: str, data: object) -> dict:
    response = requests.post(f"{API_URL}{endpoint}", json=data, headers=_headers(), timeout=30)
    response.raise_for_status()
    return response.json()


def get(endpoint: str) -> dict:
    response = requests.get(f"{API_URL}{endpoint}", headers=_headers(), timeout=30)
    response.raise_for_status()
    return response.json()


def put(endpoint: str, data: object) -> dict:
    response = requests.put(f"{API_URL}{endpoint}", json=data, headers=_headers(), timeout=30)
    response.raise_for_status()
    return response.json()


def delete(endpoint: str) -> dict:
    response = requests.delete(f"{API_URL}{endpoint}", headers=_headers(), timeout=30)
    response.raise_for_status()
    if not response.content:
        return {}
    return response.json()
