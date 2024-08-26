from pydantic_settings import BaseSettings
from typing import Optional


class Config(BaseSettings):
    DB_USER: str = "postgres"
    DB_PASSWORD: str = "1234"
    DB_HOST: str = "localhost"
    DB_NAME: str = "blog_db"
    DB_PORT: int = 5432
    SECRET_KEY: Optional[str] = None
    API_KEY: Optional[str] = None

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
