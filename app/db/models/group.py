from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from app.db.base_class import Base
from uuid import uuid4
from app.db.models.associations import user_group, group_role


class Group(Base):
    __tablename__ = "groups"

    id = Column(String, primary_key=True, default=lambda: str(uuid4()))
    name = Column(String, nullable=False, unique=True)

    users = relationship("User", secondary=user_group, back_populates="groups")
    roles = relationship("Role", secondary=group_role, back_populates="groups")
