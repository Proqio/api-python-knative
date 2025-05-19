import json
import logging
import datetime as dt
import hvac
import toml

from ._environment_variables import (
    Environment,
    vault_addr,
    vault_token,
    environment,
    log_level,
)


def get_application_name() -> str:
    with open("pyproject.toml", "r", encoding="utf-8") as file:
        pyproject_data = toml.load(file)
        return pyproject_data["tool"]["poetry"]["name"]


logging.basicConfig(level=log_level)

vault_client = hvac.Client(url=vault_addr, token=vault_token)
vault_client.is_authenticated()

vault_engine_name: str = f"proqio-mlops-{environment}"
