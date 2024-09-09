from typing import List
from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db.models.group import Group
from app.schemas.user import UserCreate
from app.db.models.user import User
from app.core.security import get_password_hash
from app.services.auth_service import verify_token

def create_user(db: Session, user_in: UserCreate, is_admin: bool):
    existing_user = get_user_by_email(db, user_in.email)
    if existing_user:
        return None

    hashed_password = get_password_hash(user_in.password)
    db_user = User(email=user_in.email, hashed_password=hashed_password)

    group_name = "client"
    if is_admin:
        group_name = "admin"

    group_client = db.query(Group).filter(Group.name == group_name).first()
    if group_client:
        db_user.groups.append(group_client)

    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()


def check_permission(required_role: str):
    def wrapper(user: User = Depends(verify_token)):

        if len(user.groups) > 0:
            for group in user.groups:
                for role in group.roles:
                    if role.name == required_role:
                        return True
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not enough permissions"
        )
    return wrapper


def get_user_permissions(user: User) -> List[str]:
    permissions = set()
    for group in user.groups:
        for role in group.roles:
            role_base = '_'.join(role.name.split('_')[:-1])

            for policy in role.policies:
                if policy.can_create:
                    permissions.add(f"{role_base}_create")
                if policy.can_read:
                    permissions.add(f"{role_base}_read")
                if policy.can_update:
                    permissions.add(f"{role_base}_update")
                if policy.can_delete:
                    permissions.add(f"{role_base}_delete")
    return list(permissions)
