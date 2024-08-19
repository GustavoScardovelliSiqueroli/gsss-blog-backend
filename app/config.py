from pydantic_settings import BaseSettings


class Config(BaseSettings):
    db_user: str = "postgre"
    db_password: str = "1234"
    db_host: str = "localhost"
    db_name: str = "blog_db"
    db_port: int = 3306
