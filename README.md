# API Sensor Gateway

The purpose of this REST API project is to provide a scalable and secure gateway for sensor data. This API manages sensor metadata and data for the MLOps platform. The API is built using FastAPI and is deployed using Docker in several kubernetes clusters.

This component has the following dependencies:
* Kafka
* PostgreSQL


## Quick Start

Deploy local development environment using Docker and Docker Compose.

```bash
docker-compose up
```

Install dependencies using Poetry.

```bash
poetry install
```

Create Postgres tables.

```bash
poetry run dac create-tables
```

Create Postgres static data.

```bash
poetry run dac create-static-data
```

Create Minio file bucket with AWS CLI.

```bash
aws --endpoint-url http://localhost:9000 s3 mb s3://proqio-local-file
```

Run the FastAPI server using Poetry.

```bash
poetry run app/main.py
```

Open your browser and go to http://localhost:5000/docs to see the Swagger UI.


## Development

How to create a 'client' test object in the database?

```bash
curl -X 'POST' \
  'http://0.0.0.0:5000/api/v1/client' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "client_uuid": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
  "client_id": "test",
  "name": "test",
  "status": "enabled",
  "registration_date": "2025-02-08T11:57:48.662Z",
  "audit_date": "2025-02-08T11:57:48.662Z"
}'
```

How to create a 'project' test object in the database?

```bash
curl -X 'POST' \
  'http://0.0.0.0:5000/api/v1/project' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "project_uuid": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
  "project_id": "test",
  "client_uuid": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
  "name": "test",
  "description": "test",
  "status": "enabled",
  "registration_date": "2025-02-08T11:58:16.091Z",
  "audit_date": "2025-02-08T11:58:16.091Z"
}'
```

How to create an 'instrument' test object in the database?

```bash
curl -X 'POST' \
  'http://localhost:5000/api/v1/instrument' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "instrument_uuid": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
  "instrument_id": "test",
  "project_uuid": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
  "status": "enabled",
  "registration_date": "2025-02-11T23:04:58.709Z",
  "audit_date": "2025-02-11T23:04:58.709Z"
}'
```

How to create a 'fileGroup' test object in the database?

```bash
curl -X 'POST' \
  'http://0.0.0.0:5000/api/v1/fileGroup' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "file_group_uuid": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
  "project_uuid": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
  "name": "test",
  "description": "test",
  "visible": true,
  "audit_date": "2025-02-08T11:53:32.894Z"
}'
```