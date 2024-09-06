from pydantic import BaseModel


class PlanSignPetRequest(BaseModel):
    pet_id: str
    plan_id: str

class PlanSignPetResponse(BaseModel):
    message: str
