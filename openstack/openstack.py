from flask import json
import requests
from datetime import datetime
import re


def getToken(username: str, password: str, projectId: str, identityEndpoint: str) -> list:
    url = f"{identityEndpoint}/auth/tokens"
    headers = {"Content-Type": "application/json"}
    data = {
        "auth": {
            "identity": {
                "methods": [
                    "password"
                ],
                "password": {
                    "user": {
                        "name": username,
                        "password": password
                    }
                }
            },
            "scope": {
                "project": {
                    "id": projectId
                }
            }
        }
    }
    response = requests.post(url=url, headers=headers, json=data)
    response.raise_for_status()
    r = response.json()
    return [r["token"]["id"], r["token"]["expires_at"]]
