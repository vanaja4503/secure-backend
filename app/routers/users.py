from fastapi import APIRouter, Depends

from app.dependencies.auth import (
    get_current_user,
    require_admin
)

from app.schemas.user import UserResponse


router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@router.get("/me", response_model=UserResponse)
def get_profile(
    current_user=Depends(get_current_user)
):
    return current_user


@router.get("/admin")
def admin_dashboard(
    current_user=Depends(require_admin)
):
    return {
        "message": "Welcome Admin",
        "username": current_user.username,
        "role": current_user.role
    }