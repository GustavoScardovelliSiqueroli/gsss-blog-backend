from app.config import Config
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import async_sessionmaker

config = Config()


async_connection_string = "postgresql+asyncpg://{}:{}@{}:{}/{}".format(
    config.DB_USER,
    config.DB_PASSWORD,
    config.DB_HOST,
    config.DB_PORT,
    config.DB_NAME,
)

async_engine = create_async_engine(async_connection_string, echo=True)
async_session = async_sessionmaker(async_engine, class_=AsyncSession)

Base = declarative_base()
