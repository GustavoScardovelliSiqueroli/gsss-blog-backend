# pyright: reportAttributeAccessIssue=false
import bcrypt
from app.config import Config
from app.domain.repository_interfaces.user_repository_interface import (
    UserRepositoryInterface,
)
from app.domain.models.user import User
from datetime import datetime, timedelta, timezone
from typing import Optional
import jwt

config = Config()


class UserCase:
    def __init__(self, repository: UserRepositoryInterface):
        self.repository = repository

    async def login_user(self, username: str, password: str) -> Optional[str]:
        user = await self.repository.get_by_username(username)
        if not user:
            return None
        if not self.__verify_password(password, user.password):
            return None
        token: str = self.__generate_jwt_token(user)
        return token

    async def register_user(self, data: User, secret_key: str) -> Optional[User]:
        if secret_key != config.SECRET_KEY:
            return None
        data.password = self.__hash_password(data.password)
        data.created_at = datetime.now()
        return await self.repository.create(data)

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
            "user_id": user.id,
            "username": user.username,
            "exp": datetime.now(timezone.utc) + timedelta(hours=24),
        }
        token: str = jwt.encode(payload, config.SECRET_KEY, algorithm="HS256")  # type:ignore
        return token
