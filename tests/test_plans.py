def test_sign_pet_to_plan_valid(client, token_with_role_client, token_with_role_admin, clear_db):
    client_token = token_with_role_client
    admin_token = token_with_role_admin

    pet1 = client.post(
        "/pets/",
        json={"name": "Rex", "age": 2, "weight": 1.2, "species": "Dog"},
        headers={"Authorization": f"Bearer {client_token}"}
    )

    pet1_id = pet1.json()["id"]

    pet2 = client.post(
        "/pets/",
        json={"name": "Nina", "age": 2, "weight": 0.600, "species": "Cat"},
        headers={"Authorization": f"Bearer {client_token}"}
    )

    pet2_id = pet2.json()["id"]

    plan = client.post(
        "/pets_plan/",
        headers={"Authorization": f"Bearer {admin_token}"},
        json={"name": "Plan test", "max_pets": 2, "price": 10.0},
    )

    plan_id = plan.json()["id"]

    response1 = client.post(
        "/plans/sign_pet/",
        headers={"Authorization": f"Bearer {client_token}"},
        json={"pet_id": pet1_id, "plan_id": plan_id},
    )

    assert response1.status_code == 200
    assert response1.json()["message"] == "Pet successfully signed to the plan."

    response2 = client.post(
        "/plans/sign_pet/",
        headers={"Authorization": f"Bearer {client_token}"},
        json={"pet_id": pet2_id, "plan_id": plan_id},
    )

    assert response2.status_code == 200
    assert response2.json()["message"] == "Pet successfully signed to the plan."


def test_sign_pet_to_plan_max_pets_exceeded(client, token_with_role_client, token_with_role_admin, clear_db):
    client_token = token_with_role_client
    admin_token = token_with_role_admin

    pet1 = client.post(
        "/pets/",
        json={"name": "Rex", "age": 2, "weight": 1.2, "species": "Dog"},
        headers={"Authorization": f"Bearer {client_token}"}
    )

    pet1_id = pet1.json()["id"]

    pet2 = client.post(
        "/pets/",
        json={"name": "Nina", "age": 2, "weight": 0.600, "species": "Cat"},
        headers={"Authorization": f"Bearer {client_token}"}
    )

    pet2_id = pet2.json()["id"]

    pet3 = client.post(
        "/pets/",
        json={"name": "Nina", "age": 2, "weight": 0.600, "species": "Cat"},
        headers={"Authorization": f"Bearer {client_token}"}
    )

    pet3_id = pet3.json()["id"]

    plan = client.post(
        "/pets_plan/",
        headers={"Authorization": f"Bearer {admin_token}"},
        json={"name": "Plan test", "max_pets": 2, "price": 10.0},
    )

    plan_id = plan.json()["id"]
    count_max = plan.json()["max_pets"]

    client.post(
        "/plans/sign_pet/",
        headers={"Authorization": f"Bearer {client_token}"},
        json={"pet_id": pet1_id, "plan_id": plan_id},
    )

    client.post(
        "/plans/sign_pet/",
        headers={"Authorization": f"Bearer {client_token}"},
        json={"pet_id": pet2_id, "plan_id": plan_id},
    )

    response = client.post(
        "/plans/sign_pet/",
        headers={"Authorization": f"Bearer {client_token}"},
        json={"pet_id": pet3_id, "plan_id": plan_id},
    )

    assert response.status_code == 400
    assert response.json()["detail"] == f"Plan has reached its limit of {count_max} pets."

