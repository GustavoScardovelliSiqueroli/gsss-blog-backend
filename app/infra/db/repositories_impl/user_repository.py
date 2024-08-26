# pyright: reportReturnType=false
from sqlalchemy import Select
from typing import Any
from app.infra.db.database import async_session
from app.domain.models.user import User
from app.domain.repository_interfaces.user_repository_interface import (
    UserRepositoryInterface,
)
from typing import Optional


class UserRepository(UserRepositoryInterface):
    async def get_all(self) -> list[Optional[User]]:
        async with async_session() as session:
            stmt: ... = Select(User)
            results = await session.execute(stmt)
            return results.scalars().all()

    async def get_by_username(self, username: str) -> Optional[User]:
        async with async_session() as session:
            stmt: ... = Select(User).where(User.username == username)
            results = await session.execute(stmt)
            return results.scalar()

    async def create(self, data: User) -> User:
        async with async_session() as session:
            async with session.begin():
                session.add(data)
            await session.commit()
            await session.refresh(data)
            return data

    async def get_by_id(self, id: Any) -> User:
        ...

    async def ate(self, id: Any, data: User) -> User:
        ...

    async def delete(self, id: Any) -> User:
        ...

    async def update(self, id: Any, data: User) -> User:
        ...
