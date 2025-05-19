import sys
import uuid
from fastapi.testclient import TestClient
from fastapi import status

from dac import DatabaseAsCode
from dac.schema.proqio_mlops import ClientStatus

sys.path.append("app")

from app.main import app
from app._utils import postgres_engine

client = TestClient(app)
database_as_code = DatabaseAsCode(postgres_engine)
database_as_code.create_tables()


def test_client():
    response = client.post(
        url="/api/v1/client",
        json={
            "client_id": str(uuid.uuid4()),
            "name": "name",
            "status": ClientStatus.enabled.value,
            "registration_date": "1997-07-16T19:20:30+01:00",
        },
    )
    assert response.status_code == status.HTTP_201_CREATED
    client_uuid: uuid.UUID = response.json()["client_uuid"]
    response = client.get(
        url=f"/api/v1/client/{client_uuid}",
    )
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["client_uuid"] == client_uuid
    response = client.patch(
        url=f"/api/v1/client/{client_uuid}",
        json={
            "status": ClientStatus.disabled.value,
        },
    )
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["status"] == ClientStatus.disabled.value
    response = client.get(
        url=f"/api/v1/client/{client_uuid}",
    )
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["status"] == ClientStatus.disabled.value
    response = client.get(
        url=f"/api/v1/clients",
    )
    assert response.status_code == status.HTTP_200_OK
    assert (
        len(
            [
                client
                for client in response.json()
                if client["client_uuid"] == client_uuid
            ]
        )
        == 1
    )
    response = client.delete(
        url=f"/api/v1/client/{client_uuid}",
    )
    assert response.status_code == status.HTTP_200_OK
    response = client.get(
        url=f"/api/v1/client/{client_uuid}",
    )
    assert response.status_code == status.HTTP_404_NOT_FOUND
