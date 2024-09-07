from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas.user import UserCreate, UserResponse
from app.services.user_service import create_user
from app.db.session import get_db

router = APIRouter()

@router.post("/client", response_model=UserResponse, summary="Register user client", response_description="Service to register user client in sign in")
def register_user_client(user_in: UserCreate, db: Session = Depends(get_db)):
    user = create_user(db=db, user_in=user_in, is_admin=False)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with this email already exists",
        )
    return user

@router.post("/admin", response_model=UserResponse, summary="Register user admin", response_description="Service to register user admin in sign in")
def register_user_admin(user_in: UserCreate, db: Session = Depends(get_db)):
    # breakpoint()
    user = create_user(db=db, user_in=user_in, is_admin=True)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with this email already exists",
        )
    return user
