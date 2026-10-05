from fastapi import FastAPI

from app.database import Base, engine
from app.models import user
from app.routers import auth, users

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Secure Backend API",
    version="0.1.0"
)

app.include_router(auth.router)
app.include_router(users.router)


@app.get("/")
def root():
    return {
        "message": "Secure Backend API is running"
    }