def test_create_group(client, token_with_role_admin, clear_db):
    admin_token = token_with_role_admin

    response = client.post(
        "/groups",
        headers={"Authorization": f"Bearer {admin_token}"},
        json={"name": "Test Group"},
    )

    assert response.status_code == 200
    assert response.json()["name"] == "Test Group"

def test_update_group(client, token_with_role_admin, clear_db):
    admin_token = token_with_role_admin

    role_response = client.post(
        "/groups",
        headers={"Authorization": f"Bearer {admin_token}"},
        json={"name": "Test Group"},
    )
    role_id = role_response.json()["id"]

    response = client.put(
        f"/groups/{role_id}",
        headers={"Authorization": f"Bearer {admin_token}"},
        json={"name": "Updated Group"},
    )

    assert response.status_code == 200
    assert response.json()["name"] == "Updated Group"

def test_delete_group(client, token_with_role_admin, clear_db):
    admin_token = token_with_role_admin

    role_response = client.post(
        "/groups",
        headers={"Authorization": f"Bearer {admin_token}"},
        json={"name": "Test Group"},
    )
    role_id = role_response.json()["id"]

    response = client.delete(
        f"/groups/{role_id}",
        headers={"Authorization": f"Bearer {admin_token}"},
    )

    assert response.status_code == 200
    assert response.json() == {"ok": True}

def test_get_group(client, token_with_role_admin, clear_db):
    admin_token = token_with_role_admin

    role_response = client.post(
        "/groups",
        headers={"Authorization": f"Bearer {admin_token}"},
        json={"name": "Test Group"})

    role_id = role_response.json()["id"]

    response = client.get(
        f"/groups/{role_id}",
        headers={"Authorization": f"Bearer {admin_token}"}
    )

    assert response.status_code == 200

    assert response.json()["name"] == "Test Group"


def test_add_role_to_group(client, token_with_role_admin, clear_db):
    admin_token = token_with_role_admin

    group_response = client.post(
        "/groups",
        headers={"Authorization": f"Bearer {admin_token}"},
        json={"name": "Test Group"},
    )
    group_id = group_response.json()["id"]

    role_response = client.post(
        "/roles",
        headers={"Authorization": f"Bearer {admin_token}"},
        json={"name": "Test Role"},
    )

    role_id = role_response.json()["id"]

    response = client.post(
        f"/groups/{group_id}/{role_id}/add_role",
        headers={"Authorization": f"Bearer {admin_token}"}
    )

    assert response.status_code == 200
    assert response.json() == {"ok": True}

def test_remove_role_from_group(client, token_with_role_admin, clear_db):
    admin_token = token_with_role_admin

    group_response = client.post(
        "/groups",
        headers={"Authorization": f"Bearer {admin_token}"},
        json={"name": "Test Group"},
    )
    group_id = group_response.json()["id"]

    role_response = client.post(
        "/roles",
        headers={"Authorization": f"Bearer {admin_token}"},
        json={"name": "Test Role"},
    )

    role_id = role_response.json()["id"]

    client.post(
        f"/groups/{group_id}/{role_id}/add_role",
        headers={"Authorization": f"Bearer {admin_token}"}
    )

    response = client.post(
        f"/groups/{group_id}/{role_id}/remove_role",
        headers={"Authorization": f"Bearer {admin_token}"}
    )

    assert response.status_code == 200
    assert response.json() == {"ok": True}

def test_add_user_to_group(client, token_with_role_admin, clear_db):
    admin_token = token_with_role_admin

    group_response = client.post(
        "/groups",
        headers={"Authorization": f"Bearer {admin_token}"},
        json={"name": "Test Group"},
    )
    group_id = group_response.json()["id"]

    response = client.post(
        f"/groups/{group_id}/add_user",
        headers={"Authorization": f"Bearer {admin_token}"}
    )

    assert response.status_code == 200
    assert response.json() == {"ok": True}

def test_remove_user_from_group(client, token_with_role_admin, clear_db):
    admin_token = token_with_role_admin

    group_response = client.post(
        "/groups",
        headers={"Authorization": f"Bearer {admin_token}"},
        json={"name": "Test Group"},
    )
    group_id = group_response.json()["id"]

    client.post(
        f"/groups/{group_id}/add_user",
        headers={"Authorization": f"Bearer {admin_token}"}
    )

    response = client.post(
        f"/groups/{group_id}/remove_user",
        headers={"Authorization": f"Bearer {admin_token}"}
    )

    assert response.status_code == 200
    assert response.json() == {"ok": True}
