def test_create_role(client, token_with_role_admin, clear_db):
    admin_token = token_with_role_admin

    response = client.post(
        "/roles",
        headers={"Authorization": f"Bearer {admin_token}"},
        json={"name": "Test Role"},
    )

    assert response.status_code == 200
    assert response.json()["name"] == "Test Role"

def test_update_role(client, token_with_role_admin, clear_db):
    admin_token = token_with_role_admin

    role_response = client.post(
        "/roles",
        headers={"Authorization": f"Bearer {admin_token}"},
        json={"name": "Test Role"},
    )
    role_id = role_response.json()["id"]

    response = client.put(
        f"/roles/{role_id}",
        headers={"Authorization": f"Bearer {admin_token}"},
        json={"name": "Updated Role"},
    )

    assert response.status_code == 200
    assert response.json()["name"] == "Updated Role"

def test_delete_role(client, token_with_role_admin, clear_db):
    admin_token = token_with_role_admin

    role_response = client.post(
        "/roles",
        headers={"Authorization": f"Bearer {admin_token}"},
        json={"name": "Test Role"},
    )
    role_id = role_response.json()["id"]

    response = client.delete(
        f"/roles/{role_id}",
        headers={"Authorization": f"Bearer {admin_token}"},
    )

    assert response.status_code == 200
    assert response.json() == {"ok": True}

def test_get_role(client, token_with_role_admin, clear_db):
    admin_token = token_with_role_admin

    role_response = client.post(
        "/roles",
        headers={"Authorization": f"Bearer {admin_token}"},
        json={"name": "Test Role"},
    )
    role_id = role_response.json()["id"]

    response = client.get(
        f"/roles/{role_id}",
        headers={"Authorization": f"Bearer {admin_token}"}
    )

    assert response.status_code == 200
    assert response.json()["name"] == "Test Role"
