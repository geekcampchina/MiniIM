import unittest

from miniim.protocol import MiniIMFieldsHandler, MiniIMField
from common import hlog
from util import to_hex_string


class MiniIMFieldTest(unittest.TestCase):
    def test_slice_data(self):
        print('\n')

        hex_data = [
            0x00, 0x03, 0x4C, 0x79, 0x75,
            0x01, 0x00,
        ]

        expected_results = [
            [0x00],
            [0x03],
            [0x4C, 0x79, 0x75],
            [0x01],
            [0x00],
            [],
        ]

        recv_data = bytes(hex_data)
        hlog.var('recv_data', to_hex_string(recv_data))

        handler = MiniIMFieldsHandler()

        remain_bb = recv_data

        for result in expected_results:
            step = len(result)
            self.assertEqual(handler.slice_data(remain_bb, step), bytes(result))
            remain_bb = remain_bb[step:]

    def test_slice_field(self):
        print('\n')

        hex_data = [
            0x00, 0x03, 0x4C, 0x79, 0x75,
            0x01, 0x00,
        ]

        expected_result = [
            bytes([0x00, 0x03, 0x4C, 0x79, 0x75]),
            bytes([0x01, 0x00]),
        ]

        recv_data = bytes(hex_data)
        hlog.var('recv_data', to_hex_string(recv_data))

        handler = MiniIMFieldsHandler()

        field_bb = handler.slice_field(recv_data)
        self.assertIsNotNone(field_bb)
        self.assertEqual(field_bb, expected_result[0])

        field_bb = handler.slice_field(recv_data[len(field_bb):])
        self.assertIsNotNone(field_bb)
        self.assertEqual(field_bb, expected_result[1])

    def test_run(self):
        print('\n')

        hex_data = [
            0x00, 0x03, 0x4C, 0x79, 0x75,
            0x01, 0x00,
        ]

        expected_result = [
            MiniIMField(ftype=0, flen=3, fvalue=bytes([0x4C, 0x79, 0x75])),
            MiniIMField(ftype=1, flen=0, fvalue=bytes([])),
        ]

        recv_data = bytes(hex_data)
        hlog.var('recv_data', to_hex_string(recv_data))

        result = []
        handler = MiniIMFieldsHandler()

        handler.run(recv_data, result)

        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
