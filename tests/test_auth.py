from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_login(db_session):
    client.post("/users/", json={"email": "user@example.com", "password": "password"})
    response = client.post("/login", json={"email": "user@example.com", "password": "password"})
    assert response.status_code == 200
    assert "access_token" in response.json()

    response = client.post("/login", json={"email": "user@test.com", "password": "password"})
    assert response.status_code == 401
