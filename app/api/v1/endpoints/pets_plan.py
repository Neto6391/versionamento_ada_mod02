from fastapi import APIRouter, Depends
from pytest import Session

from app.schemas.pets_plan import PetPlanCreate, PetPlanResponse, PetPlanUpdate
from app.services.pets_plan_service import PetPlanService
from app.services.user_service import check_permission
from app.db.session import get_db

router = APIRouter()

@router.post("/", response_model=PetPlanResponse, dependencies=[Depends(check_permission(required_role="plan_create"))])
def create_pet_plan(plan: PetPlanCreate, db: Session = Depends(get_db)):
    service: PetPlanService = PetPlanService(db)
    return service.create_plan(plan)

@router.get("/{plan_id}", response_model=PetPlanResponse, dependencies=[Depends(check_permission(required_role="plan_read"))])
def get_pet_plan(plan_id: str, db: Session = Depends(get_db)):
    service: PetPlanService = PetPlanService(db)
    return service.get_plan(plan_id)

@router.put("/{plan_id}", response_model=PetPlanResponse, dependencies=[Depends(check_permission(required_role="plan_update"))])
def update_pet_plan(plan_id: str, plan: PetPlanUpdate, db: Session = Depends(get_db)):
    service: PetPlanService = PetPlanService(db)
    return service.update_plan(plan_id, plan)

@router.delete("/{plan_id}", dependencies=[Depends(check_permission(required_role="plan_delete"))])
def delete_pet_plan(plan_id: str, db: Session = Depends(get_db)):
    service: PetPlanService = PetPlanService(db)
    service.delete_plan(plan_id)
    return {"message": "Plan deleted successfully"}
