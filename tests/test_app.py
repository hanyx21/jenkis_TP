from app.app import app

def test_ping():
    client = app.test_client()
    resp = client.get("/ping")
    assert resp.status_code == 200
    data = resp.get_json()
    assert data["ok"] is True
