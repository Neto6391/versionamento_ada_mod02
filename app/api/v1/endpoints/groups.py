from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.models.user import User
from app.services.auth_service import verify_token
from app.services.group_service import GroupService
from app.schemas.group import GroupCreate, GroupInDBBase, GroupUpdate
from app.db.session import get_db
from app.services.user_service import check_permission

router = APIRouter()


@router.post("/", response_model=GroupInDBBase, dependencies=[Depends(check_permission(required_role="group_create"))])
def create_group(group_in: GroupCreate, db: Session = Depends(get_db)):
    group_service = GroupService(db)
    return group_service.create_group(group_in)


@router.put("/{group_id}", response_model=GroupInDBBase, dependencies=[Depends(check_permission(required_role="group_update"))])
def update_group(group_id: str, group_in: GroupUpdate, db: Session = Depends(get_db)):
    group_service = GroupService(db)
    return group_service.update_group(group_id, group_in)


@router.delete("/{group_id}", dependencies=[Depends(check_permission(required_role="group_delete"))])
def delete_group(group_id: str, db: Session = Depends(get_db)):
    group_service = GroupService(db)
    return group_service.delete_group(group_id)


@router.get("/{group_id}", response_model=GroupInDBBase, dependencies=[Depends(check_permission(required_role="group_read"))])
def get_group(group_id: str, db: Session = Depends(get_db)):
    group_service = GroupService(db)
    return group_service.get_group(group_id)

@router.post("/{group_id}/{role_id}/add_role", dependencies=[Depends(check_permission(required_role="group_in_role_create"))])
def add_role_to_group(group_id: str, role_id: str, db: Session = Depends(get_db)):
    group_service = GroupService(db)
    return group_service.add_role_to_group(group_id, role_id)


@router.post("/{group_id}/{role_id}/remove_role", dependencies=[Depends(check_permission(required_role="group_out_role_delete"))])
def remove_role_from_group(group_id: str, role_id: str, db: Session = Depends(get_db)):
    group_service = GroupService(db)

    return group_service.remove_role_from_group(group_id, role_id)


@router.post("/{group_id}/add_user", dependencies=[Depends(check_permission(required_role="group_in_user_create"))])
def add_user_to_group(group_id: str, db: Session = Depends(get_db), current_user: User = Depends(verify_token)):
    group_service = GroupService(db)
    return group_service.add_user_to_group(group_id, current_user)


@router.post("/{group_id}/remove_user", dependencies=[Depends(check_permission(required_role="group_out_user_delete"))])
def remove_user_from_group(group_id: str, db: Session = Depends(get_db), current_user: User = Depends(verify_token)):
    group_service = GroupService(db)
    return group_service.remove_user_from_group(group_id, current_user)
