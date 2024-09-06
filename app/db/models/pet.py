from uuid import uuid4
from sqlalchemy import Column, String, ForeignKey, Float, INTEGER
from sqlalchemy.orm import relationship
from app.db.base_class import Base
from app.db.models.associations import pet_plan_pet


class Pet(Base):
    __tablename__ = "pets"

    id = Column(String, primary_key=True, default=lambda: str(uuid4()))
    name = Column(String, index=True, nullable=False)
    age = Column(INTEGER, index=True, nullable=False)
    weight = Column(Float, index=True, nullable=False)
    species = Column(String, nullable=False)
    owner_id = Column(String, ForeignKey("users.id"), nullable=False)

    owner = relationship("User", back_populates="pets")
    plans = relationship('PetPlan', secondary=pet_plan_pet, back_populates='pets')
