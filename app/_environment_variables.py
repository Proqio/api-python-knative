from decouple import config
from enum import StrEnum


class Environment(StrEnum):
    LOCAL = "local"
    CICD = "cicd"
    DEV = "dev"
    PROD = "prod"
    CENTRAL = "central"


class LogLevel(StrEnum):
    CRITICAL = "CRITICAL"
    FATAL = "FATAL"
    ERROR = "ERROR"
    WARN = "WARN"
    WARNING = "WARNING"
    INFO = "INFO"
    DEBUG = "DEBUG"
    NOTSET = "NOTSET"


class UvicornLogLevel(StrEnum):
    critial = "critical"
    error = "error"
    warning = "warning"
    info = "info"
    debug = "debug"
    trace = "trace"


vault_addr: str = config("VAULT_ADDR", cast=str)
vault_token: str = config("VAULT_TOKEN", cast=str)
environment: Environment = config("ENVIRONMENT", default=Environment.LOCAL, cast=str)
port: int = config("PORT", cast=int, default=5000)
log_level: LogLevel = config("LOG_LEVEL", cast=str, default=LogLevel.INFO)
uvicorn_log_level: UvicornLogLevel = config(
    "UVICORN_LOG_LEVEL", cast=str, default=UvicornLogLevel.info
)
workers: int = config("WORKERS", cast=int, default=1)
