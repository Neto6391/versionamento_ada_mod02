from sqlalchemy.orm import Session
from app.db.models.group import Group
from app.db.models.role import Role
from app.db.models.user import User
from app.schemas.group import GroupCreate, GroupUpdate
from fastapi import HTTPException


class GroupService:
    def __init__(self, db: Session):
        self.db = db

    def get_group(self, group_id: str):
        group = self.db.query(Group).filter(Group.id == group_id).first()
        if not group:
            raise HTTPException(status_code=404, detail="Group not found")
        return group

    def get_role(self, role_id: str):
        role = self.db.query(Role).filter(Role.id == role_id).first()
        if not role:
            raise HTTPException(status_code=404, detail="Role not found")
        return role

    def create_group(self, group_in: GroupCreate):
        new_group = Group(name=group_in.name)
        self.db.add(new_group)
        self.db.commit()
        self.db.refresh(new_group)
        return new_group

    def update_group(self, group_id: str, group_in: GroupUpdate):
        group = self.get_group(group_id)
        group.name = group_in.name
        self.db.commit()
        self.db.refresh(group)
        return group

    def delete_group(self, group_id: str):
        group = self.get_group(group_id)
        self.db.delete(group)
        self.db.commit()
        return {"ok": True}

    def add_role_to_group(self, group_id: str, role_id: str):
        group = self.get_group(group_id)
        role = self.get_role(role_id)
        if not group or not role:
            raise HTTPException(status_code=404, detail="Group or Role not found")
        group.roles.append(role)
        self.db.commit()
        return {"ok": True}

    def remove_role_from_group(self, group_id: str, role_id: str):
        group = self.get_group(group_id)
        role = self.get_role(role_id)
        if not group or not role:
            raise HTTPException(status_code=404, detail="Group or Role not found")
        group.roles.remove(role)
        self.db.commit()
        return {"ok": True}

    def add_user_to_group(self, group_id: str, user: User):
        group = self.get_group(group_id)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        group.users.append(user)
        self.db.commit()
        return {"ok": True}

    def remove_user_from_group(self, group_id: str, user: User):
        group = self.get_group(group_id)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        group.users.remove(user)
        self.db.commit()
        return {"ok": True}
