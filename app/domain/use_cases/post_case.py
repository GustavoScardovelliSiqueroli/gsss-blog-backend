from app.domain.repository_interfaces.post_repository_interface import (
    PostRepositoryInterface,
)
from app.domain.models.post import Post


class PostCase:
    def __init__(self, repository: PostRepositoryInterface):
        self.repository = repository

    async def create_post(self, data: Post) -> Post:
        return await self.repository.create(data)

    async def get_all_posts(self) -> list[Post]:
        return await self.repository.get_all()
