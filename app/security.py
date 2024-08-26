import jwt  # PyJWT
from jwt import ExpiredSignatureError, InvalidTokenError
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from app.config import Config
from app.domain.use_cases.user_case import UserCase
from app.infra.db.repositories_impl.user_repository import UserRepository
from app.domain.models.user import User

config = Config()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")
credentials_exception = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Could not validate credentials",
    headers={"WWW-Authenticate": "Bearer"},
)


def get_user_case() -> UserCase:
    repository = UserRepository()
    return UserCase(repository=repository)


async def get_current_user(
    token: str = Depends(oauth2_scheme), user_case: UserCase = Depends(get_user_case)
) -> User:
    try:
        if config.API_KEY is None:
            raise credentials_exception

        payload = jwt.decode(token, config.API_KEY, algorithms=["HS256"])

        user_id: str | None = payload.get("user_id")
        if user_id is None:
            raise credentials_exception

        user = await user_case.repository.get_by_id(user_id)
        if user is None:
            raise credentials_exception

    except (ExpiredSignatureError, InvalidTokenError) as e:
        raise credentials_exception from e

    return user
