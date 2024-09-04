import os
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv(dotenv_path='.env')


class Settings(BaseSettings):
    SECRET_KEY: str = os.getenv("SECRET_KEY")
    ALGORITHM: str = "HS256"
    DATABASE_URL: str = os.getenv("DATABASE_URL")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 60))


settings = Settings()
