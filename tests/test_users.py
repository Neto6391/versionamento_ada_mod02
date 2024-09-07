def test_create_user(client, db_session):
    response = client.post("/users/client", json={"email": "user@example.com", "password": "password"})
    assert response.status_code == 200
    assert response.json()["email"] == "user@example.com"
