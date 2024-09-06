from sqlalchemy.orm import Session
from app.db.models.pet import Pet
from app.db.models.pet_plan import PetPlan
from app.db.models.associations import pet_plan_pet
from sqlalchemy import and_


class PlanService:
    def __init__(self, db: Session):
        self.db = db

    def sign_pet_to_plan(self, user_id: str, pet_id: str, plan_id: str):
        pet_user = self.db.query(Pet).filter(and_(Pet.id == pet_id, Pet.owner_id == user_id)).first()
        if not pet_user:
            raise Exception("Pet not found or not owned by the user")

        pet_plan = self.db.query(PetPlan).filter(PetPlan.id == plan_id).first()
        if not pet_plan:
            raise Exception("Plan not found")

        pets_in_plan = self.db.query(pet_plan_pet).filter(pet_plan_pet.c.plan_id == plan_id).count()

        if pets_in_plan >= pet_plan.max_pets:
            raise Exception(f"Plan has reached its limit of {pet_plan.max_pets} pets.")

        insert_pet_plan = pet_plan_pet.insert().values(pet_id=pet_id, plan_id=plan_id)
        self.db.execute(insert_pet_plan)
        self.db.commit()

        return {"message": "Pet successfully signed to the plan."}

    def cancel_pet_plan(self, user_id: str, pet_id: str, plan_id: str):
        pet = self.db.query(Pet).filter(and_(Pet.id == pet_id, Pet.owner_id == user_id)).first()
        if not pet:
            raise Exception("Pet not found or not owned by the user")

        remove_out_plan = pet_plan_pet.delete().where(and_(pet_plan_pet.c.pet_id == pet_id, pet_plan_pet.c.plan_id == plan_id))
        result = self.db.execute(remove_out_plan)

        if result.rowcount == 0:
            raise Exception("No such association found between pet and plan.")

        self.db.commit()

        return {"message": "Plan cancelled for the pet."}
