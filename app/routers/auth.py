from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.services.auth_service import (
    authenticate_user,
    create_user_token,
    register_user
)
from app.schemas.user import UserCreate, UserResponse


router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.post("/register", response_model=UserResponse)
def register(
    user: UserCreate,
    db: Session = Depends(get_db)
):
    new_user, error = register_user(
        db=db,
        username=user.username,
        email=user.email,
        password=user.password
    )

    if error:
        raise HTTPException(
            status_code=400,
            detail=error
        )

    return new_user


@router.post("/login")
def login(
    username: str,
    password: str,
    db: Session = Depends(get_db)
):
    user = authenticate_user(
        db=db,
        username=username,
        password=password
    )

    if not user:
        raise HTTPException(
            status_code=401,
            detail="Invalid username or password"
        )

    access_token = create_user_token(user)

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }
