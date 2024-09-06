def test_create_plan_pets(client, token_with_role_admin, clear_db):
    admin_token = token_with_role_admin

    response = client.post(
        "/pets_plan/",
        headers={"Authorization": f"Bearer {admin_token}"},
        json={"name": "Plan test", "max_pets": 1, "price": 10.0},
    )

    assert response.status_code == 200
    assert response.json()["name"] == "Plan test"

def test_update_plan_pets(client, token_with_role_admin, clear_db):
    admin_token = token_with_role_admin

    pets_plan_response = client.post(
        "/pets_plan/",
        headers={"Authorization": f"Bearer {admin_token}"},
        json={"name": "Plan test", "max_pets": 1, "price": 10.0},
    )

    pets_plan_id = pets_plan_response.json()["id"]

    response = client.put(
        f"/pets_plan/{pets_plan_id}",
        headers={"Authorization": f"Bearer {admin_token}"},
        json={"name": "Updated Plan"},
    )

    assert response.status_code == 200
    assert response.json()["name"] == "Updated Plan"

def test_delete_plan_pets(client, token_with_role_admin, clear_db):
    admin_token = token_with_role_admin

    response = client.post(
        "/pets_plan/",
        headers={"Authorization": f"Bearer {admin_token}"},
        json={"name": "Plan test", "max_pets": 1, "price": 10.0},
    )

    response_id = response.json()["id"]

    response = client.delete(
        f"/pets_plan/{response_id}",
        headers={"Authorization": f"Bearer {admin_token}"},
    )

    assert response.status_code == 200
    assert response.json() == {"message": "Plan deleted successfully"}

def test_get_plan_pets(client, token_with_role_admin, clear_db):
    admin_token = token_with_role_admin

    pets_plan_response = client.post(
        "/pets_plan/",
        headers={"Authorization": f"Bearer {admin_token}"},
        json={"name": "Plan test", "max_pets": 1, "price": 10.0},
    )

    pets_plan_id = pets_plan_response.json()["id"]

    response = client.get(
        f"/pets_plan/{pets_plan_id}",
        headers={"Authorization": f"Bearer {admin_token}"}
    )

    assert response.status_code == 200
    assert response.json()["name"] == "Plan test"
