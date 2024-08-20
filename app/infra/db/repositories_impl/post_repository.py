from sqlalchemy import Select
from typing import Any
from app.infra.db.database import async_session
from app.domain.models.post import Post
from app.domain.repository_interfaces.post_repository_interface import (
    PostRepositoryInterface,
)


class PostRepository(PostRepositoryInterface):
    async def get_all(self) -> list[Post]:
        async with async_session() as session:
            stmt: ... = Select(Post)
            results = await session.execute(stmt)
            return results.scalars().all()  # type: ignore

    async def create(self, data: Post) -> Post:
        async with async_session() as session:
            async with session.begin():
                session.add(data)
            await session.commit()
            await session.refresh(data)
            return data

    async def get_by_id(self, id: Any) -> Post:
        ...

    async def update(self, id: Any, data: Post) -> Post:
        ...

    async def delete(self, id: Any) -> Post:
        ...
