from sqlalchemy import INTEGER, Column, Float, String
from app.db.base_class import Base
from uuid import uuid4


class PetPlan(Base):
    __tablename__ = "pets_plan"

    id = Column(String, primary_key=True, default=lambda: str(uuid4()))
    name = Column(String, nullable=False, unique=True)
    max_pets = Column(INTEGER, nullable=False, unique=True)
    price = Column(Float, nullable=False, unique=True)
