from typing import Optional
from pydantic import BaseModel

class PetPlanCreate(BaseModel):
    name: str
    max_pets: int
    price: float

class PetPlanUpdate(BaseModel):
    name: Optional[str] = None
    max_pets: Optional[int] = None
    price: Optional[float] = None

class PetPlanResponse(BaseModel):
    id: str
    name: str
    max_pets: int
    price: float

