from sqlalchemy import Column, Integer, String
from app.infra.db.database import Base


class Post(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50))


def teste(teste: str) -> str:
    return teste


teste(True)
teste({"ola": "teste"})
