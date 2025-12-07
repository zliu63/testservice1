# testservice1

FastAPI service skeleton for testservice1. Uses SQLAlchemy + Alembic for schema management.

## Structure
- `src/app` — FastAPI app modules (api/core/models/services/db/schemas)
- `src/tests` — unit and integration tests
- `migrations` — Alembic migrations
- `infra` — app-level infra (Dockerfile, compose overrides, etc.)
- `scripts` — local tooling (lint, dev server helpers)

## Notes
- Add dependencies in `pyproject.toml` (or `requirements.txt`).
- Configure DB URL via `.env`.
- Manage schema: `alembic revision --autogenerate` then `alembic upgrade head`.

## Run & test greeting API (with chelsydb Postgres)

Prereqs
- Python 3.12/3.11 (avoid 3.13 for pydantic wheels).
- chelsydb Postgres running (from `/Users/ziyangliu/Projects/Cherries/chelsydb`): `docker-compose up -d`.

1) Install deps
```
cd /Users/ziyangliu/Projects/Cherries/testservice1
python3.12 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip setuptools wheel
pip install -r requirements.txt   # installs -e ../chelsydb too
```

2) Run API
```
python -m uvicorn app.main:app --app-dir src --reload --host 0.0.0.0 --port 8000 --env-file .env
```

3) Test greeting endpoint (writes payload.message into testtbl1)
```
curl -X PUT "http://localhost:8000/cherries/greeting" \
  -H "Content-Type: application/json" \
  -d '{"message":"Hello Chelsy"}'
```
Expected: `{"status":"ok","echoed":"Hello Chelsy"}`

4) Verify DB (optional)
```
docker exec -it chelsydb-postgres psql -U testuser -d chelsydb -c 'SELECT * FROM testtbl1;'
```
