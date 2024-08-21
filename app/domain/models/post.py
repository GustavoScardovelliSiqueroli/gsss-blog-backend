from sqlalchemy import Column, Integer, String, DateTime
from app.infra.db.database import Base


class Post(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(50))
    content = Column(String(500))
    created_at = Column(DateTime)
