from dataclasses import dataclass


@dataclass(frozen=True)
class UserCredentials:
    email: str
    password: str
    name: str
    