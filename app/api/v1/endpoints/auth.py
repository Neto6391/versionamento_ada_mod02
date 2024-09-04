from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.services.user_service import get_user_by_email
from app.schemas.auth import LoginForm, Token

from app.core.security import verify_password, create_access_token
from app.db.session import get_db

router = APIRouter()

@router.post("/", response_model=Token)
def login_for_access_token(
    form_data: LoginForm, db: Session = Depends(get_db)
):
    user = get_user_by_email(db, email=form_data.email)
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(data={"sub": user.email, "scopes": []})
    return {"access_token": access_token, "token_type": "bearer"}
