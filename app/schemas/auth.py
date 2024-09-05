from pydantic import BaseModel, EmailStr
from typing import List

class LoginForm(BaseModel):
    email: EmailStr
    password: str

class TokenData(BaseModel):
    email: str
    scopes: List[str]

class Token(BaseModel):
    access_token: str
    token_type: str
