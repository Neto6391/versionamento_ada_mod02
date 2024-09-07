

from sqlalchemy import Column, String, DateTime
from app.db.base_class import Base
import uuid
from datetime import datetime, timezone

class TokenBlacklist(Base):
    __tablename__ = "token_blacklist"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()), index=True)
    token = Column(String, unique=True, index=True)
    blacklisted_on = Column(DateTime, default=datetime.now(timezone.utc))
