import json

from miniim.protocol import MiniIMField
from util import to_hex, to_bytes


class Login:
    def __init__(self):
        self.user = ''
        self.password = ''


class MiniIMFrame:
    def __init__(self):
        self.action_type = 0
        self.payload_len = 0
        self.payload: list[MiniIMField] = []
        self.login = Login()

    def dump(self) -> bytearray:
        bb = bytearray()

        bb.append(self.action_type)
        bb += to_bytes(self.payload_len, 3)

        for field in self.payload:
            bb += field.dump()

        return bb

    def __str__(self):
        output_dict = {
            'action_type': self.action_type,
            'payload_len': self.payload_len,
            'login': self.login
        }

        return json.dumps(output_dict, indent=4, ensure_ascii=False)
