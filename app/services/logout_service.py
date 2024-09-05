from sqlalchemy.orm import Session
from app.db.models.token_black_list import TokenBlacklist


def blacklist_token(db: Session, token: str):
    blacklisted_token = TokenBlacklist(token=token)
    db.add(blacklisted_token)
    db.commit()
