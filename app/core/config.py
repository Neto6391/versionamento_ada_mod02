import os
from pydantic_settings  import BaseSettings
from dotenv import load_dotenv

load_dotenv(dotenv_path='.env')

class Settings(BaseSettings):
    PROJECT_NAME: str = "PetPlan"
    ALGORITHM: str = "HS256"
    DATABASE_URL: str = os.getenv("DATABASE_URL")

settings = Settings()
