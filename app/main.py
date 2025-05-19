from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import toml

from app._environment_variables import (
    Environment,
    environment,
    port,
    uvicorn_log_level,
    workers,
)

if environment == Environment.CENTRAL:
    from app.routers import healthz
else:
    from app.routers import (
        healthz,
        sample
)


def get_version() -> str:
    with open("pyproject.toml", "r", encoding="utf-8") as file:
        pyproject_data = toml.load(file)
        return pyproject_data["tool"]["poetry"]["version"]


app = FastAPI(
    title="Proqio: api-sensor-sample",
    description=open("README.md", mode="r").read(),
    version=get_version(),
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

if environment == Environment.CENTRAL:
    app.include_router(healthz.router)
    app.include_router(instrument_data.router)
else:
    app.include_router(healthz.router)
    app.include_router(sample.router)

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=port,
        log_level=uvicorn_log_level,
        reload=True,
        workers=workers,
    )
