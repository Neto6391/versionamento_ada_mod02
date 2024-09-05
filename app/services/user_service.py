from sqlalchemy.orm import Session
from app.schemas.user import UserCreate
from app.db.models.user import User
from app.core.security import get_password_hash

def create_user(db: Session, user_in: UserCreate):
    existing_user = get_user_by_email(db, user_in.email)
    if existing_user:
        return None

    hashed_password = get_password_hash(user_in.password)
    db_user = User(email=user_in.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()
