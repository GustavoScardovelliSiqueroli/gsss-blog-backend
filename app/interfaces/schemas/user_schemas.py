from dataclasses import dataclass


@dataclass
class TokenResponse:
    token: str


@dataclass
class UserLogin:
    username: str
    password: str


@dataclass
class UserRegister:
    username: str
    password: str
    key: str


@dataclass
class UserRegisterResponse:
    message: str
