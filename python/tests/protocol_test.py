import unittest

from miniim import MiniIMDecoder
from common import hlog
from util import to_hex_string


class ProtocolTest(unittest.TestCase):
    def test_login(self):
        print('\n')

        hex_data = [
            0x01, 0x00, 0x00, 0x0B,
            0x00, 0x03, 0x4C, 0x79, 0x75,
            0x01, 0x04, 0x61, 0x62, 0x63, 0x64
        ]

        # 01 00 00 0B 00 03 4C 79 75 01 04 61 62 63 64
        recv_data = bytes(hex_data)
        hlog.var('recv_data', to_hex_string(recv_data))

        decoder = MiniIMDecoder(recv_data)
        frame = decoder.run()

        self.assertEqual(frame.payload, {0: 'Lyu', 1: 'abcd'})

    def test_validate_header(self):
        print('\n')

        hex_data = [
            ([0x01, 0x00, 0x00], False),
            ([0x01, 0x00, 0x00, 0x0B], True),
            ([0x01, 0x00, 0x00, 0x0B, 0x00, 0x03, 0x4C, 0x79, 0x75, 0x01, 0x04, 0x61, 0x62, 0x63, 0x64], True)
        ]

        for hd, expect_result in hex_data:
            recv_data = bytes(hd)

            decoder = MiniIMDecoder(recv_data)
            self.assertEqual(decoder.validate_header(), expect_result)

    def test_validate_payload_len(self):
        print('\n')

        hex_data = [
            ([0x01, 0x00, 0x00, 0x00], True),
            ([0x01, 0x00, 0x00, 0x0B, 0x00, 0x03, 0x4C, 0x79, 0x75, 0x01, 0x04, 0x61, 0x62, 0x63, 0x64], True)
        ]

        for hd, expect_len in hex_data:
            recv_data = bytes(hd)

            decoder = MiniIMDecoder(recv_data)
            self.assertEqual(decoder.validate_payload_len(), expect_len)

    def test_slice(self):
        hex_data = [
            0x01, 0x00, 0x00, 0x0B,
            0x00, 0x03, 0x4C, 0x79, 0x75, 0x01, 0x04, 0x61, 0x62, 0x63, 0x64
        ]

        recv_data = bytes(hex_data)
        decoder = MiniIMDecoder(recv_data)

        self.assertEqual(decoder.slice_action_type(), 0x01)
        self.assertEqual(decoder.slice_payload_len(), bytes([0x00, 0x00, 0x0B]))
        self.assertEqual(decoder.slice_payload(),
                         bytes([0x00, 0x03, 0x4C, 0x79, 0x75, 0x01, 0x04, 0x61, 0x62, 0x63, 0x64]))

    def test_validate_fields(self):
        hex_data = [
            0x01, 0x00, 0x00, 0x0B,
            0x00, 0x03, 0x4C, 0x79, 0x75, 0x01, 0x04, 0x61, 0x62, 0x63, 0x64
        ]

        recv_data = bytes(hex_data)
        decoder = MiniIMDecoder(recv_data)

        result = dict()
        payload = bytes([0x00, 0x03, 0x4C, 0x79, 0x75, 0x01, 0x04, 0x61, 0x62, 0x63, 0x64])
        decoder.decode_fields(payload, result, 0)

        self.assertEqual(result, {0: 'Lyu', 1: 'abcd'})

    def test_validate_slice_fields(self):
        pass


if __name__ == '__main__':
    unittest.main()
