def test_create_pet(client, token_with_role_client, clear_db):
    test_user_token = token_with_role_client
    response = client.post(
        "/pets/",
        json={"name": "Rex", "age": 2, "weight": 1.2, "species": "Dog"},
        headers={"Authorization": f"Bearer {test_user_token}"}
    )
    assert response.status_code == 200
    assert response.json()["name"] == "Rex"

def test_get_pet(client, token_with_role_client, clear_db):
    test_user_token = token_with_role_client
    test_pet_create = client.post(
        "/pets/",
        json={"name": "Rex", "age": 2, "weight": 1.2, "species": "Dog"},
        headers={"Authorization": f"Bearer {test_user_token}"}
    )

    test_pet_create_id = test_pet_create.json()["id"]

    response = client.get(f"/pets/{test_pet_create_id}", headers={"Authorization": f"Bearer {test_user_token}"})
    assert response.status_code == 200
    assert response.json()["id"] == test_pet_create_id

def test_update_pet(client, token_with_role_client, clear_db,):
    test_user_token = token_with_role_client

    test_pet_create = response = client.post(
        "/pets/",
        json={"name": "Rex", "species": "Dog", "age": 2, "weight": 1.2},
        headers={"Authorization": f"Bearer {test_user_token}"}
    )
    test_pet_create = test_pet_create.json()["id"]
    response = client.put(
        f"/pets/{test_pet_create}",
        json={"name": "Max", "species": "Cat", "age": 1, "weight": 0.700},
        headers={"Authorization": f"Bearer {test_user_token}"}
    )
    assert response.status_code == 200
    assert response.json()["name"] == "Max"

def test_delete_pet(client, token_with_role_client, clear_db):
    test_user_token = token_with_role_client
    test_pet = response = client.post(
        "/pets/",
        json={"name": "Rex", "species": "Dog", "age": 2, "weight": 1.2},
        headers={"Authorization": f"Bearer {test_user_token}"}
    )
    test_pet = test_pet.json()["id"]
    response = client.delete(f"/pets/{test_pet}", headers={"Authorization": f"Bearer {test_user_token}"})
    assert response.status_code == 204
