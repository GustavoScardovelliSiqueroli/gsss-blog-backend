from sqlalchemy import Column, Integer, String, DateTime, Text, ForeignKey, UUID
from app.infra.db.database import Base


class Post(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True, index=True)
    user_id: ... = Column(UUID, ForeignKey("users.id"), index=True)
    title = Column(String(50), nullable=False)
    content = Column(Text, nullable=False)
    created_at = Column(DateTime, nullable=False)
