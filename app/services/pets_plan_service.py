from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.db.models.pet_plan import PetPlan
from app.schemas.pets_plan import PetPlanCreate, PetPlanUpdate


class PetPlanService:
    def __init__(self, db: Session):
        self.db = db

    def create_plan(self, plan_data: PetPlanCreate):
        new_plan = PetPlan(**plan_data.model_dump())
        self.db.add(new_plan)
        self.db.commit()
        return new_plan

    def get_plan(self, plan_id: str):
        return self.db.query(PetPlan).filter(PetPlan.id == plan_id).first()

    def update_plan(self, plan_id: str, plan_update: PetPlanUpdate):
        plan = self.get_plan(plan_id)
        if not plan:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Plan not found")
        if plan_update.model_dump().get("name") is not None:
            plan.name = plan_update.name
        if plan_update.model_dump().get("max_pets") is not None:
            plan.max_pets = plan_update.max_pets
        if plan_update.model_dump().get("price") is not None:
            plan.price = plan_update.price

        self.db.commit()
        self.db.refresh(plan)
        return plan

    def delete_plan(self, plan_id: str):
        plan = self.get_plan(plan_id)
        if not plan:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Plan not found")
        self.db.delete(plan)
        self.db.commit()
