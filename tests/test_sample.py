import sys
import uuid
from fastapi.testclient import TestClient
from fastapi import status

sys.path.append("app")

from app.main import app

client = TestClient(app)


def test_client():
    sample_name: str = "Sam"
    response = client.get(
        url=f"/sample/{sample_name}",
    )
    assert response.status_code == status.HTTP_200_OK
