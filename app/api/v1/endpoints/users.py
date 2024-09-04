from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas.user import UserCreate, UserResponse
from app.services.user_service import create_user
from app.db.session import get_db

router = APIRouter()

@router.post("/", response_model=UserResponse, summary="Register user", response_description="Service to register user in sign in")
def register_user(user_in: UserCreate, db: Session = Depends(get_db)):
    user = create_user(db=db, user_in=user_in)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with this email already exists",
        )
    return user
