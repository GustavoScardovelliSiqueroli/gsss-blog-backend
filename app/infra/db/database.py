from app.config import Config
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.ext.asyncio import AsyncSession

config = Config()

async_connection_string = "postgresql+asyncpg://{}:{}@{}/{}".format(
    config.db_user,
    config.db_password,
    config.db_host,
    config.db_port,
)

async_engine = create_async_engine(async_connection_string, echo=True)
async_session = sessionmaker(async_engine, class_=AsyncSession)

Base = declarative_base()
