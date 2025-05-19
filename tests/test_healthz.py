import sys
from fastapi.testclient import TestClient
from fastapi import status

sys.path.append("app")

from app.main import app

client = TestClient(app)


def test_healthz_readiness():
    response = client.get("/healthzReadiness")
    assert response.status_code == status.HTTP_200_OK


def test_healthz_liveness():
    response = client.get("/healthzLiveness")
    assert response.status_code == status.HTTP_200_OK


def test_healthz_startup():
    response = client.get("/healthzStartup")
    assert response.status_code == status.HTTP_200_OK
