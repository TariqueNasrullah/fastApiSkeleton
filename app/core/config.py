from pydantic import AnyHttpUrl, PostgresDsn
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str

    # Example 60 minutes * 24 hours * 8 days = 8 days [ 60 * 24 * 8]
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 10
    SERVER_HOST: AnyHttpUrl = "http://localhost:8000"

    SECRET_GITHUB_CLIENT_ID: str
    SECRET_GITHUB_CLIENT_SECRET: str

    POSTGRES_SERVER: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
