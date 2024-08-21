from dataclasses import dataclass
from datetime import datetime


@dataclass
class PostResponse:
    id: int
    title: str
    content: str
    created_at: datetime


@dataclass
class PostCreate:
    title: str
    content: str
