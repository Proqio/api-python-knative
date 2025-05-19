ARG PYTHON_VERSION=3.12
ARG DEBIAN_VERSION=bookworm

FROM python:${PYTHON_VERSION}-slim-${DEBIAN_VERSION} AS builder

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    POETRY_NO_INTERACTION=1 \
    POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_CREATE=false

ARG POETRY_VERSION=2.1.1

RUN apt-get update && apt-get install -y curl \
    && curl -sSL https://install.python-poetry.org | python3 - \
    && apt-get remove -y curl \
    && apt-get autoremove -y \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

ENV PATH="$PATH:$POETRY_HOME/bin"

WORKDIR /app

ARG POETRY_REPOSITORY=dummy
ARG PIPSERVER_URL=https://pypi.org/simple
ARG PIPSERVER_USERNAME=dummy
ARG PIPSERVER_PASSWORD=dummy

RUN poetry config repositories.$POETRY_REPOSITORY $PIPSERVER_URL
RUN poetry config http-basic.$POETRY_REPOSITORY $PIPSERVER_USERNAME $PIPSERVER_PASSWORD

COPY pyproject.toml poetry.lock* /app/

RUN --mount=type=cache,target=/opt/poetry/cache \
    poetry install --only main --no-root

COPY . .

RUN --mount=type=cache,target=/opt/poetry/cache \
    poetry install --only main

FROM python:${PYTHON_VERSION}-slim-${DEBIAN_VERSION} AS production

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

ARG UID=10001
RUN adduser \
    --disabled-password \
    --gecos "" \
    --home "/nonexistent" \
    --shell "/sbin/nologin" \
    --no-create-home \
    --uid "${UID}" \
    appuser

ARG PYTHON_VERSION=3.12

COPY --from=builder /usr/local/lib/python${PYTHON_VERSION}/site-packages /usr/local/lib/python${PYTHON_VERSION}/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin

USER appuser

COPY . .

EXPOSE 5000

CMD python3 -u app/main.py