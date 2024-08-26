# pyright: reportAttributeAccessIssue=false
from app.domain.repository_interfaces.post_repository_interface import (
    PostRepositoryInterface,
)
from app.domain.models.post import Post
from datetime import datetime


class PostCase:
    def __init__(self, repository: PostRepositoryInterface):
        self.repository = repository

    async def create_post(self, data: Post, id_user: str) -> Post:
        data.created_at = datetime.now()
        data.id_user = id_user
        return await self.repository.create(data)

    async def get_all_posts(self) -> list[Post]:
        return await self.repository.get_all()
