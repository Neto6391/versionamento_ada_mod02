from fastapi import FastAPI
from app.api.v1.endpoints import users
from app.db.session import SessionLocal, engine
from app.db.base_class import Base
from dotenv import load_dotenv

load_dotenv(dotenv_path='.env')

app = FastAPI(
    title="PetPlan API",
     description="API PetPlan StartUp",
    version="1.0.0",
    contact={
        "name": "Neto6391",
        "url": "http://example.com",
        "email": "mail@exemple.com",
    },
)
app.include_router(users.router, prefix="/users", tags=["users"])


if __name__ == "__main__":
    host = os.getenv("HOST", "127.0.0.1")
    port = int(os.getenv("PORT"))
    uvicorn.run(app, host=host, port=port, reload=True)