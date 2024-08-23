from abc import ABC, abstractmethod
from app.domain.models.user import User
from typing import Any, Optional


class UserRepositoryInterface(ABC):
    @abstractmethod
    async def get_by_username(self, username: str) -> Optional[User]:
        pass

    @abstractmethod
    async def get_all(self) -> list[Optional[User]]:
        pass

    @abstractmethod
    async def get_by_id(self, id: Any) -> Optional[User]:
        pass

    @abstractmethod
    async def create(self, data: User) -> User:
        pass

    @abstractmethod
    async def update(self, id: Any, data: User) -> User:
        pass

    @abstractmethod
    async def delete(self, id: Any) -> User:
        pass
