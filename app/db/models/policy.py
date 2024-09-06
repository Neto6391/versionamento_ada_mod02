from sqlalchemy import Column, String, Boolean
from sqlalchemy.orm import relationship
from app.db.base_class import Base
from uuid import uuid4
from app.db.models.associations import role_policy

class Policy(Base):
    __tablename__ = "policies"

    id = Column(String, primary_key=True, default=lambda: str(uuid4()))
    name = Column(String, nullable=False, unique=True)
    can_create = Column(Boolean, default=False)
    can_read = Column(Boolean, default=False)
    can_update = Column(Boolean, default=False)
    can_delete = Column(Boolean, default=False)

    roles = relationship("Role", secondary=role_policy, back_populates="policies")
