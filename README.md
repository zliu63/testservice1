# testservice1

FastAPI service skeleton for testservice1. Uses SQLAlchemy + Alembic for schema management.

## Structure
- `src/app` — FastAPI app modules (api/core/models/services/db/schemas)
- `src/tests` — unit and integration tests
- `migrations` — Alembic migrations
- `infra` — app-level infra (Dockerfile, compose overrides, etc.)
- `scripts` — local tooling (lint, dev server helpers)

## Quick start (dev)
- Add dependencies in `pyproject.toml` (or `requirements.txt`).
- Configure DB URL via `.env`.
- Run app: `uvicorn app.main:app --reload` (after wiring entrypoint in `main.py`).
- Manage schema: `alembic revision --autogenerate` then `alembic upgrade head`.
