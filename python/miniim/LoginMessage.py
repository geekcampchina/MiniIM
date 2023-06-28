from dataclasses import dataclass


@dataclass
class LoginMessage:
    user: str
    password: str
