import os

class Settings:
    PROJECT_NAME: str = "PetPlan"
    SQLALCHEMY_DATABASE_URI: str = os.getenv("DATABASE_URL", "sqlite:///./database/petplan.db")
