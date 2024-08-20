from abc import ABC, abstractmethod
from app.domain.models.post import Post
from typing import Any


class PostRepositoryInterface(ABC):
    @abstractmethod
    async def get_all(self) -> list[Post]:
        pass

    @abstractmethod
    async def get_by_id(self, id: Any) -> Post:
        pass

    @abstractmethod
    async def create(self, data: Post) -> Post:
        pass

    @abstractmethod
    async def update(self, id: Any, data: Post) -> Post:
        pass

    @abstractmethod
    async def delete(self, id: Any) -> Post:
        pass
