import json
from dataclasses import dataclass, asdict
from happy_python import dict_to_pretty_json


@dataclass
class LoginMessage:
    user: str
    password: str
    client: str

    def asjson(self) -> str:
        return dict_to_pretty_json(asdict(self))
