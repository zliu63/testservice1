from starlette.testclient import TestClient

from app.main import app


def test_put_greeting_returns_ok_and_echoes_message():
    client = TestClient(app)
    payload = {"message": "Hello Chelsy"}

    resp = client.put("/cherries/greeting", json=payload)

    assert resp.status_code == 200
    assert resp.json() == {"status": "ok", "echoed": payload["message"]}


def test_put_greeting_requires_message():
    client = TestClient(app)

    resp = client.put("/cherries/greeting", json={})

    assert resp.status_code == 422
