from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.role import Role, RoleCreate, RoleUpdate
from app.services.role_service import RoleService
from app.db.session import get_db
from app.services.user_service import check_permission

router = APIRouter()

@router.post("/", response_model=Role, dependencies=[Depends(check_permission(required_role="role_create"))])
def create_role(role_in: RoleCreate, db: Session = Depends(get_db)):
    role_service = RoleService(db)
    return role_service.create_role(role_in)

@router.put("/{role_id}", response_model=Role, dependencies=[Depends(check_permission(required_role="role_update"))])
def update_role(role_id: str, role_in: RoleUpdate, db: Session = Depends(get_db)):
    role_service = RoleService(db)
    return role_service.update_role(role_id, role_in)

@router.delete("/{role_id}", dependencies=[Depends(check_permission(required_role="role_delete"))])
def delete_role(role_id: str, db: Session = Depends(get_db)):
    role_service = RoleService(db)
    role_service.delete_role(role_id)
    return {"ok": True}

@router.get("/{role_id}", response_model=Role, dependencies=[Depends(check_permission(required_role="role_read"))])
def get_role(role_id: str, db: Session = Depends(get_db)):
    role_service = RoleService(db)
    return role_service.get_role(role_id)
