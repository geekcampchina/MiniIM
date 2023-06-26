import json

from util import to_hex


class Login:
    def __init__(self):
        self.user = ''
        self.password = ''


class MiniIMFrame:
    def __init__(self):
        self.action_type = 0
        self.payload_len = 0
        self.payload = dict()
        self.login = Login()

    def __str__(self):
        output_dict = {
            'action_type': to_hex(self.action_type),
            'payload_len': self.payload_len,
            'login': self.login.__dict__
        }

        return json.dumps(output_dict, indent=4, ensure_ascii=False)
