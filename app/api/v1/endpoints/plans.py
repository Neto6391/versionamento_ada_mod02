from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.models.user import User
from app.schemas.plan import PlanSignPetRequest, PlanSignPetResponse
from app.services.auth_service import verify_token
from app.services.plans_service import PlanService
from app.services.user_service import check_permission
from app.db.session import get_db

router = APIRouter()

@router.post("/sign_pet", response_model=PlanSignPetResponse, dependencies=[Depends(check_permission(required_role="plan_sign_pet_create"))])
def sign_pet_to_plan(request: PlanSignPetRequest, db: Session = Depends(get_db), user: User = Depends(verify_token)):
    plan_service = PlanService(db)
    try:
        result = plan_service.sign_pet_to_plan(user.id, request.pet_id, request.plan_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    return result
