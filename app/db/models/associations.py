from sqlalchemy import Column, String, ForeignKey, Table
from app.db.base_class import Base


user_group = Table(
    "user_group",
    Base.metadata,
    Column("user_id", String, ForeignKey("users.id"), primary_key=True),
    Column("group_id", String, ForeignKey("groups.id"), primary_key=True)
)

group_role = Table(
    "group_role", Base.metadata,
    Column("group_id", String, ForeignKey("groups.id"), primary_key=True),
    Column("role_id", String, ForeignKey("roles.id"), primary_key=True)
)

role_policy = Table(
    "role_policy", Base.metadata,
    Column("role_id", String, ForeignKey("roles.id"), primary_key=True),
    Column("policy_id", String, ForeignKey("policies.id"), primary_key=True)
)
