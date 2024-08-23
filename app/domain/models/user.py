from app.infra.db.database import Base
from sqlalchemy import Column, String, UUID, DateTime


class User(Base):
    __tablename__ = "users"
    id: ... = Column(UUID, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)
    created_at = Column(DateTime, nullable=False)
