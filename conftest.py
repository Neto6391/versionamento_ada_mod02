import uuid
import pytest
import sys
import os

from fastapi.testclient import TestClient

from app.db.models.group import Group
from app.db.models.policy import Policy
from app.db.models.role import Role
from app.main import app
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.db.base_class import Base


sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))


@pytest.fixture(scope="module")
def client():
    client = TestClient(app)
    return client

@pytest.fixture(scope='session')
def test_db():
    engine = create_engine(os.environ['DATABASE_URL'], connect_args={"check_same_thread": False})

    Base.metadata.create_all(bind=engine)

    TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    yield TestingSessionLocal

    Base.metadata.drop_all(bind=engine)

@pytest.fixture(scope='function')
def db_session(test_db):
    db = test_db()
    db.commit()
    yield db
    db.close()

@pytest.fixture(scope='function')
def token_with_role_admin(client, populate_db):
    client.post("/users/admin", json={"email": "admin@example.com", "password": "password"})
    response = client.post("/auth", json={"email": "admin@example.com", "password": "password"})
    auth_data = response.json()
    token = auth_data.get("access_token")
    return token

@pytest.fixture(scope='function', autouse=True)
def populate_db(db_session):
    policies = [
        Policy(id=str(uuid.uuid4()), name="create", can_create=True, can_read=False, can_update=False, can_delete=False),
        Policy(id=str(uuid.uuid4()), name="read", can_create=False, can_read=True, can_update=False, can_delete=False),
        Policy(id=str(uuid.uuid4()), name="update", can_create=False, can_read=False, can_update=True, can_delete=False),
        Policy(id=str(uuid.uuid4()), name="delete", can_create=False, can_read=False, can_update=False, can_delete=True)
    ]
    db_session.add_all(policies)

    # Create roles
    roles = [
        Role(id=str(uuid.uuid4()), name=name) for name in [
            "pet_create", "pet_read", "pet_update", "pet_delete",
            "plan_create", "plan_read", "plan_update", "plan_delete",
            "plan_sign_pet_create", "plan_sign_pet_read", "plan_sign_pet_update", "plan_sign_pet_delete",
            "role_create", "role_read", "role_update",
            "role_delete", "group_create", "group_read", "group_update", "group_delete", "group_in_user_create",
            "group_out_user_delete", "group_in_role_create", "group_out_role_delete"
        ]
    ]
    db_session.add_all(roles)

    # Create groups
    groups = [
        Group(id=str(uuid.uuid4()), name="client"),
        Group(id=str(uuid.uuid4()), name="admin")
    ]
    db_session.add_all(groups)

    # Associate roles with policies
    for role in roles:
        policy = next((p for p in policies if p.name == role.name.split('_')[-1]), None)
        if policy:
            role.policies.append(policy)

    # Associate roles with groups
    client_group = next(g for g in groups if g.name == 'client')
    admin_group = next(g for g in groups if g.name == 'admin')

    client_roles = ['pet_create', 'pet_read', 'pet_update', 'pet_delete',
                    'plan_sign_pet_create', 'plan_sign_pet_read', 'plan_sign_pet_update', 'plan_sign_pet_delete']
    admin_roles = client_roles + ['plan_create', 'plan_read', 'plan_update', 'plan_delete', 'role_create', 'role_read', 'role_update', 'role_delete', 'group_create', 'group_read', 'group_update', 'group_delete', 'group_in_user_create', 'group_out_user_delete', "group_in_role_create", "group_out_role_delete"]

    for role in roles:
        if role.name in client_roles:
            client_group.roles.append(role)
        if role.name in admin_roles:
            admin_group.roles.append(role)
    db_session.commit()


@pytest.fixture(scope='function', autouse=True)
def clear_db(db_session):
    for table in reversed(Base.metadata.sorted_tables):
        db_session.execute(table.delete())
    db_session.commit()
