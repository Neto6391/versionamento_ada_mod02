def test_login(client):
    client.post("/users/client/", json={"email": "user@example.com", "password": "password"})
    response = client.post("/auth", json={"email": "user@example.com", "password": "password"})
    assert response.status_code == 200
    assert "access_token" in response.json()

    response = client.post("/auth/", json={"email": "user@test.com", "password": "password"})
    assert response.status_code == 401

def test_logout(client):
    client.post("/users/client/", json={"email": "user@example.com", "password": "password"})
    response = client.post("/auth", json={"email": "user@example.com", "password": "password"})
    auth_data = response.json()
    valid_token = auth_data.get("access_token")
    response = client.post("/auth/logout", headers={"Authorization": f"Bearer {valid_token}"})
    assert response.status_code == 200
