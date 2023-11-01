from .base import BaseModel
from sqlalchemy import Column, String, VARCHAR, Boolean


class User(BaseModel):
    __tablename__ = "users"

    id = Column(VARCHAR(), primary_key=True, index=True)
    name = Column(VARCHAR(100))
    email = Column(String, unique=True, index=True, nullable=False)
    phone = Column(VARCHAR(20), unique=True, index=True, nullable=True)
    hashed_password = Column(String, nullable=True)
    avatar = Column(String, nullable=True)
    is_active = Column(Boolean, default=True)

