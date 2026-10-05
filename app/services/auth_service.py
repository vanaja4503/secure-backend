from sqlalchemy.orm import Session

from app.models.user import User
from app.utils.security import (
    hash_password,
    verify_password,
    create_access_token
)


def register_user(
    db: Session,
    username: str,
    email: str,
    password: str
):
    existing_user = db.query(User).filter(
        User.username == username
    ).first()

    if existing_user:
        return None, "Username already exists"

    existing_email = db.query(User).filter(
        User.email == email
    ).first()

    if existing_email:
        return None, "Email already exists"

    hashed_password = hash_password(password)

    new_user = User(
        username=username,
        email=email,
        password=hashed_password,
        role="user"
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user, None


def authenticate_user(
    db: Session,
    username: str,
    password: str
):
    user = db.query(User).filter(
        User.username == username
    ).first()

    if not user:
        return None

    if not verify_password(password, user.password):
        return None

    return user


def create_user_token(user: User):
    return create_access_token(
        data={
            "sub": user.username,
            "role": user.role
        }
    )

