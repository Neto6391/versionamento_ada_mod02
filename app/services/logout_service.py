from sqlalchemy.orm import Session
from app.db.models.token_black_list import TokenBlacklist

class LogoutService:
    def __init__(self, db: Session):
        self.db = db

    def blacklist_token(self, token: str):
        blacklisted_token = TokenBlacklist(token=token)
        self.db.add(blacklisted_token)
        self.db.commit()
