# pyright: reportArgumentType = false
from app.domain.models.post import Post
from app.interfaces.schemas.post_schemas import PostResponse, PostCreate


class PostMapper:
    @staticmethod
    def entity_to_response(entity: Post) -> PostResponse:
        return PostResponse(
            id=entity.id,
            title=entity.title,
            content=entity.content,
            created_at=entity.created_at,
        )

    @staticmethod
    def create_to_entity(create: PostCreate) -> Post:
        return Post(title=create.title, content=create.content)
