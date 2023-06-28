from miniim.protocol import MiniIMFrame, MiniIMField
from miniim.protocol import MiniIMFieldsHandler
from util import to_int


class MiniIMDecoder:
    def __init__(self, recv_data: bytes):
        self.recv_data = recv_data

    def validate_header(self) -> bool:
        # [01 00 00 00]
        # [01 00 00 0B] 00 03 4C 79 75 01 04 61 62 63 64
        return len(self.recv_data) >= 4

    def validate_payload_len(self) -> bool:
        # 01 [00 00 0B] <00 03 4C 79 75 01 04 61 62 63 64>

        payload_len = to_int(self.slice_payload_len())

        total_len = len(self.recv_data)
        header_len = 4
        recv_payload_len = total_len - header_len

        # [00 00 0B] -> 11
        # <00 03 4C 79 75 01 04 61 62 63 64> -> 11
        return payload_len == recv_payload_len

    def slice_action_type(self) -> int:
        # [01] 00 00 0B 00 03 4C 79 75 01 04 61 62 63 64
        return self.recv_data[0]

    def slice_payload_len(self) -> bytes:
        # 01 [00 00 0B] 00 03 4C 79 75 01 04 61 62 63 64
        return self.recv_data[1:4]

    def slice_payload(self) -> bytes:
        # 01 00 00 0B [00 03 4C 79 75 01 04 61 62 63 64]
        return self.recv_data[4:]

    def decode_payload_len(self) -> int:
        return to_int(self.slice_payload_len())

    def decode_payload(self) -> list[MiniIMField]:
        result = list()

        field_handler = MiniIMFieldsHandler()
        field_handler.run(self.slice_payload(), result)

        return result

    def decode_action_type(self) -> int:
        return self.slice_action_type()

    def run(self) -> MiniIMFrame:
        frame = MiniIMFrame()

        frame.action_type = self.decode_action_type()

        frame.payload_len = self.decode_payload_len()

        frame.payload = self.decode_payload()

        return frame
