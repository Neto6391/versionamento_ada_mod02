from fastapi import FastAPI
from app.api.v1.endpoints import users, auth, roles, groups
from dotenv import load_dotenv
import os
import uvicorn
from app.db.models import User, Group, Role, Policy, user_group, group_role, role_policy  # noqa: F401
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
app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(roles.router, prefix="/roles", tags=["roles"])
app.include_router(groups.router, prefix="/groups", tags=["groups"])

if __name__ == "__main__":
    host = os.getenv("HOST", "127.0.0.1")
    port = int(os.getenv("PORT"))
    uvicorn.run(app, host=host, port=port, reload=True)
