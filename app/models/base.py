import datetime
from sqlalchemy import Column, DateTime, Boolean

from app.db.base_class import Base


class BaseModel(Base):
    __abstract__ = True

    now = lambda: datetime.datetime.now().replace(microsecond=0)
    is_deleted = Column(Boolean, default=False, nullable=False)
    created_at = Column(DateTime, default=now())
    updated_at = Column(DateTime, default=now())
