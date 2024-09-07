from pydantic import BaseModel


class GroupBase(BaseModel):
    name: str


class GroupCreate(GroupBase):
    pass


class GroupUpdate(GroupBase):
    pass


class GroupInDBBase(GroupBase):
    id: str
