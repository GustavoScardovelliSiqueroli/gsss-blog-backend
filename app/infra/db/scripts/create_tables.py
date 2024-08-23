import asyncio
from app.infra.db.database import async_engine, Base
from app.domain.models.user import User
from app.domain.models.post import Post

user = User
post = Post


async def create_tables():
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    await async_engine.dispose()
    print("Tables created!")


if __name__ == "__main__":
    asyncio.run(create_tables())
