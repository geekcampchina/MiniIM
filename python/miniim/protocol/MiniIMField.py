import json
from dataclasses import dataclass, asdict
from happy_python import dict_to_pretty_json


@dataclass
class MiniIMField:
    ftype: int
    flen: int
    fvalue: bytes

    def asdict(self):
        return asdict(self)

