from fastapi import FastAPI

from app.core.config import settings

from manual_db_migration.migrate import create_tables
create_tables()

app = FastAPI(title=settings.API_V1_STR)


@app.get("/")
async def root():
    return {"message": "Hello World"}
