from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from app.core.config import settings
from app.schemas.auth import TokenData
from app.services.blacklist_token_service import BlacklistTokenService


from datetime import datetime, timedelta, timezone
from app.db.session import get_db

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt


def decode_token(token: str) -> TokenData:
    # Exceção padrão para problemas com credenciais
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])

        email: str = payload.get("sub")
        scopes: list[str] = payload.get("scopes")
        exp: int = payload.get("exp")

        if email is None:
            raise credentials_exception
        exp_datetime = datetime.fromtimestamp(exp, tz=timezone.utc)
        if datetime.now(timezone.utc) > exp_datetime:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token has expired",
                headers={"WWW-Authenticate": "Bearer"},
            )

        return TokenData(email=email, scopes=scopes)

    except JWTError:
        raise credentials_exception


def verify_token(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    from app.services.user_service import get_user_by_email

    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    blacklistTokenService = BlacklistTokenService(db)
    if not blacklistTokenService.is_token_blacklisted(token):
        token_data: TokenData = decode_token(token)

        user = get_user_by_email(db, email=token_data.email)
        if user is None:
            raise credentials_exception
        return user
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="User must login in",
        headers={"WWW-Authenticate": "Bearer"},
    )
    raise credentials_exception

