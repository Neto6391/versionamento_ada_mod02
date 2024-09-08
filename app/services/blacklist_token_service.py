from sqlalchemy.orm import Session
from app.db.models.token_black_list import TokenBlacklist


class BlacklistTokenService:
    def __init__(self, db: Session) -> bool:
        self.db = db

    def is_token_blacklisted(self, token: str):
        token_has_blacklisted = self.db.query(TokenBlacklist).filter(TokenBlacklist.token == token).first()
        if token_has_blacklisted:
            return True
        return False
