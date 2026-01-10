from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health():
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json()["status"] == "ok"

def test_create_user():
    payload = {
        "email": "testuser@example.com", 
        "full_name": "Test User",
        "password": "Pwd123"
    }
    r = client.post("/users", json=payload)
    assert r.status_code in (200, 201)
    data = r.json()
    assert data["email"] == payload["email"]

def test_list_users():
    r = client.get("/users")
    assert r.status_code == 200
    assert isinstance(r.json(), list)
