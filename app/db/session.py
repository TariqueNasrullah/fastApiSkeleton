from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.config import settings

pgUrl = "postgresql://" + settings.POSTGRES_USER + ":" + settings.POSTGRES_PASSWORD + "@" + settings.POSTGRES_SERVER + "/" + settings.POSTGRES_DB
engine = create_engine(url=pgUrl, pool_pre_ping=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
