from sqlalchemy.orm import Session
from app.schemas.user import UserCreate
from app.db.models.user import User
from app.core.security import get_password_hash

def create_user(db: Session, user_in: UserCreate):
    hashed_password = get_password_hash(user_in.password)
    db_user = User(email=user_in.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
