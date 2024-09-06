from typing import Optional
from pydantic import BaseModel


class PetCreate(BaseModel):
    name: str
    age: int
    weight: float
    species: str

class PetUpdate(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    weight: Optional[float] = None
    species: Optional[str] = None

class PetResponse(BaseModel):
    id: str
    name: str
    species: str
    age: int
    weight: float
    owner_id: str
