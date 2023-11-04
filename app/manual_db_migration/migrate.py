from app.db.base_class import Base
from app.models.user import User
from app.db.session import engine


def create_tables():
    """
    create tables in the database
    """
    # just for development purposes
    # so just to make this clear - this is not an "unused import"
    # models must be imported before we call create_all method
    Base.metadata.create_all(bind=engine)
