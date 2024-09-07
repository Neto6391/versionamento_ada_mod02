from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.db.models.role import Role
from app.schemas.role import RoleCreate, RoleUpdate


class RoleService:
    def __init__(self, db: Session):
        self.db = db

    def create_role(self, role_in: RoleCreate) -> Role:
        role = Role(name=role_in.name)
        self.db.add(role)
        self.db.commit()
        self.db.refresh(role)
        return role

    def update_role(self, role_id: str, role_in: RoleUpdate) -> Role:
        role = self.db.query(Role).filter(Role.id == role_id).first()
        if not role:
            raise HTTPException(status_code=404, detail="Role not found")
        for key, value in role_in.model_dump().items():
            setattr(role, key, value)
        self.db.commit()
        self.db.refresh(role)
        return role

    def delete_role(self, role_id: str):
        role = self.db.query(Role).filter(Role.id == role_id).first()
        if not role:
            raise HTTPException(status_code=404, detail="Role not found")
        self.db.delete(role)
        self.db.commit()

    def get_role(self, role_id: str) -> Role:
        role = self.db.query(Role).filter(Role.id == role_id).first()
        if not role:
            raise HTTPException(status_code=404, detail="Role not found")
        return role
