from dataclasses import dataclass, asdict
from happy_python import dict_to_pretty_json

from miniim.protocol import MiniIMFrame, MiniIMField


@dataclass
class LoginMessage:
    user: str
    password: str
    client: str

    def dump_frame(self) -> MiniIMFrame:
        frame = MiniIMFrame()

        frame.action_type = 1

        user_bb = bytes(self.user, 'UTF-8')
        user_field = MiniIMField(ftype=0, flen=len(user_bb), fvalue=user_bb)
        frame.payload.append(user_field)
        frame.payload_len += 2 + len(user_bb)

        password_bb = bytes(self.password, 'UTF-8')
        password_field = MiniIMField(ftype=1, flen=len(password_bb), fvalue=password_bb)
        frame.payload.append(password_field)
        frame.payload_len += 2 + len(password_bb)

        client_bb = bytes(self.client, 'UTF-8')
        client_field = MiniIMField(ftype=2, flen=len(client_bb), fvalue=client_bb)
        frame.payload.append(client_field)
        frame.payload_len += 2 + len(client_bb)

        return frame

    def asjson(self) -> str:
        return dict_to_pretty_json(asdict(self))
