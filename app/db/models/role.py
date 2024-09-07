from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from app.db.base_class import Base
from uuid import uuid4
from app.db.models.associations import role_policy, group_role


class Role(Base):
    __tablename__ = "roles"

    id = Column(String, primary_key=True, default=lambda: str(uuid4()))
    name = Column(String, nullable=False, unique=True)

    groups = relationship("Group", secondary=group_role, back_populates="roles")
    policies = relationship("Policy", secondary=role_policy, back_populates="roles")
