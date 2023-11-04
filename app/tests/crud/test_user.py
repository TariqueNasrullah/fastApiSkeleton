from sqlalchemy.orm import Session

from app import crud
from app.v1.schemas.user import UserCreate


def test_create_user(db: Session) -> None:
    email = "nasrullahtarique@gmail.com"
    password = "jata"
    user_in = UserCreate(email=email, password=password)
    user = crud.user.create(db, obj_in=user_in)
    assert user.email == email
    assert hasattr(user, "hashed_password")