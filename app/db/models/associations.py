from uuid import uuid4
from sqlalchemy import Column, String, ForeignKey, Table
from app.db.base_class import Base


user_group = Table(
    "user_group",
    Base.metadata,
    Column("user_id", String, ForeignKey("users.id"), primary_key=True),
    Column("group_id", String, ForeignKey("groups.id"), primary_key=True)
)

group_role = Table(
    "group_roles", Base.metadata,
    Column("group_id", String, ForeignKey("groups.id"), primary_key=True),
    Column("role_id", String, ForeignKey("roles.id"), primary_key=True)
)

role_policy = Table(
    "role_policy", Base.metadata,
    Column("role_id", String, ForeignKey("roles.id"), primary_key=True),
    Column("policy_id", String, ForeignKey("policies.id"), primary_key=True)
)

pet_plan_pet = Table(
    "pet_plan_pet", Base.metadata,
    Column("id", String, primary_key=True, default=lambda: str(uuid4())),
    Column("pet_id", String, ForeignKey("pets.id"), nullable=False),
    Column("plan_id", String, ForeignKey("pets_plan.id"), nullable=False)
)
