from pydantic import BaseModel


class PetCreate(BaseModel):
    name: str
    age: int
    weight: float
    species: str

class PetUpdate(PetCreate):
    pass

class PetResponse(BaseModel):
    id: str
    name: str
    species: str
    age: int
    weight: float
    owner_id: str
