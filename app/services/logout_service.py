from fastapi import HTTPException, status
from app.services.blacklist_token_service import BlacklistTokenService
from sqlalchemy.orm import Session
from app.db.models.token_black_list import TokenBlacklist


class LogoutService:
    def __init__(self, db: Session):
        self.db = db

    def blacklist_token(self, token: str):
        blacklistTokenService = BlacklistTokenService(self.db)
        if not blacklistTokenService.is_token_blacklisted(token):
            blacklisted_token = TokenBlacklist(token=token)
            self.db.add(blacklisted_token)
            self.db.commit()
            return None
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User must login in",
            headers={"WWW-Authenticate": "Bearer"},
        )

