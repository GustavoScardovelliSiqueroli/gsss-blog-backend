from fastapi import APIRouter, Depends, HTTPException, status
from app.domain.repository_interfaces.user_repository_interface import (
    UserRepositoryInterface,
)
from app.infra.db.repositories_impl.user_repository import UserRepository
from app.domain.use_cases.user_case import (
    UserCase,
    AuthenticationError,
    InternalAPIError,
)
from app.interfaces.schemas.user_schemas import (
    TokenResponse,
    UserLogin,
    UserRegister,
    UserRegisterResponse,
)
from app.interfaces.mappers.user_mapper import UserMapper


def get_user_repository() -> UserRepositoryInterface:
    return UserRepository()


def get_user_case() -> UserCase:
    return UserCase(repository=get_user_repository())


router = APIRouter(prefix="", tags=["users"])


@router.post("/login", response_model=TokenResponse)
async def login(
    user_login: UserLogin, user_case: UserCase = Depends(get_user_case)
) -> TokenResponse:
    try:
        token = await user_case.login_user(
            username=user_login.username, password=user_login.password
        )
        return TokenResponse(token=token)
    except AuthenticationError as e:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(e))


@router.post("/register", response_model=UserRegisterResponse)
async def register(
    user_data: UserRegister, user_case: UserCase = Depends(get_user_case)
) -> UserRegisterResponse:
    user_domain = UserMapper.create_to_entity(user_data)
    try:
        await user_case.register_user(user_domain, user_data.key)
        return UserRegisterResponse(message="Successfully registered user")
    except InternalAPIError as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e)
        )
