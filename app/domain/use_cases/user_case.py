# pyright: reportAttributeAccessIssue=false
import uuid
import bcrypt
from app.config import Config
from app.domain.repository_interfaces.user_repository_interface import (
    UserRepositoryInterface,
)
from app.domain.models.user import User
from datetime import datetime, timedelta, timezone
import jwt

config = Config()


class AuthenticationError(Exception):
    pass


class InternalAPIError(Exception):
    pass


class UserCase:
    def __init__(self, repository: UserRepositoryInterface):
        self.repository = repository

    async def login_user(self, username: str, password: str) -> str:
        user = await self.repository.get_by_username(username)
        if not user:
            raise AuthenticationError("Invalid username or password")
        if not self.__verify_password(password, user.password):
            raise AuthenticationError("Invalid username or password")
        token: str = self.__generate_jwt_token(user)
        return token

    """
    TODO:
    verify if user arrealy exist;
    """

    async def register_user(self, data: User, secret_key: str) -> User:
        if secret_key != config.SECRET_KEY:
            raise InternalAPIError
        data.id = uuid.uuid4()
        data.password = self.__hash_password(data.password)
        data.created_at = datetime.now()
        try:
            return await self.repository.create(data)
        except Exception as e:
            raise InternalAPIError(f"Error during user creation: {str(e)}")

    async def get_all_user(self) -> list[User]:
        return await self.repository.get_all()

    def __hash_password(self, password: ...) -> str:
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password.encode("utf-8"), salt)
        return hashed_password.decode("utf-8")

    def __verify_password(self, plain_password: str, hashed_password: ...) -> bool:
        return bcrypt.checkpw(
            plain_password.encode("utf-8"), hashed_password.encode("utf-8")
        )

    def __generate_jwt_token(self, user: User) -> str:
        payload = {
            "user_id": str(user.id),
            "username": user.username,
            "exp": datetime.now(timezone.utc) + timedelta(hours=24),
        }
        token: str = jwt.encode(payload, config.API_KEY, algorithm="HS256")  # type:ignore
        return token
