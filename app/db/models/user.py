from sqlalchemy import Column, String, Boolean
from sqlalchemy.orm import relationship
from app.db.base_class import Base
from app.db.models.associations import user_group
import uuid


class User(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)

    groups = relationship("Group", secondary=user_group, back_populates="users")
    pets = relationship("Pet", back_populates="owner")
