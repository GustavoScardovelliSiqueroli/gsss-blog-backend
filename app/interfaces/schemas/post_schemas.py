from dataclasses import dataclass


@dataclass
class PostResponse:
    id: int
    title: str


@dataclass
class PostCreate:
    title: str
