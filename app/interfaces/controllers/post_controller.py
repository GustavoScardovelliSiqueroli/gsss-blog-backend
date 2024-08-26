from fastapi import APIRouter, Depends
from app.domain.use_cases.post_case import PostCase
from app.infra.db.repositories_impl.post_repository import PostRepository
from app.interfaces.schemas.post_schemas import PostResponse, PostCreate
from app.interfaces.mappers.post_mapper import PostMapper
from app.security import get_current_user
from app.domain.models.user import User
from app.domain.repository_interfaces.post_repository_interface import (
    PostRepositoryInterface,
)


router = APIRouter(prefix="/posts", tags=["post"])


def get_post_repository() -> PostRepositoryInterface:
    return PostRepository()


def get_post_case(
    repository: PostRepository = Depends(get_post_repository),
) -> PostCase:
    return PostCase(repository)


router = APIRouter(prefix="/posts", tags=["post"])


@router.get("/")
async def get_posts(post_case: PostCase = Depends(get_post_case)) -> list[PostResponse]:
    posts = await post_case.get_all_posts()
    print(posts)
    return [PostMapper.entity_to_response(post) for post in posts]


@router.post("/", response_model=PostResponse)
async def create_post(
    post_create: PostCreate,
    post_case: PostCase = Depends(get_post_case),
    user: User = Depends(get_current_user),
) -> PostResponse:
    post_domain = PostMapper.create_to_entity(post_create)
    post_db = await post_case.create_post(post_domain, user.id)
    return PostMapper.entity_to_response(post_db)
