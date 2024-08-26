# pyright: reportArgumentType = false
from app.domain.models.user import User
from app.interfaces.schemas.user_schemas import UserRegister


class UserMapper:
    @staticmethod
    def create_to_entity(create: UserRegister) -> User:
        return User(username=create.username, password=create.password)
