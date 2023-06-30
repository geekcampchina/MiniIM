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

    def dump(self) -> bytearray:
        bb = bytearray()
        bb.append(self.ftype)
        bb.append(self.flen)
        bb += self.fvalue

        return bb

