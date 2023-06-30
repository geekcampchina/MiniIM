import unittest

from common import hlog
from miniim import LoginMessage
from miniim.protocol import MiniIMDecoder
from util import to_hex_string


class LoginMessageTest(unittest.TestCase):
    def test_something(self):
        print('\n')

        hex_data = [
            0x01, 0x00, 0x00, 0x0B,
            0x00, 0x03, 0x4C, 0x79, 0x75,
            0x01, 0x04, 0x61, 0x62, 0x63, 0x64,
            0x02, 0x06, 0x74, 0x65, 0x6C, 0x6E, 0x65, 0x74,
        ]

        recv_data = bytes(hex_data)
        hlog.var('recv_data', to_hex_string(recv_data))

        decoder = MiniIMDecoder(recv_data)
        frame = decoder.run()

        self.assertEqual(len(frame.payload), 3)

        # TODO Frame->LoginMessage
        lm = LoginMessage(user=frame.payload[0].fvalue.decode('UTF-8'),
                          password=frame.payload[1].fvalue.decode('UTF-8'),
                          client=frame.payload[2].fvalue.decode('UTF-8'))
        expected_lm = LoginMessage(user='Lyu', password='abcd', client='telnet')

        self.assertEqual(lm, expected_lm)


if __name__ == '__main__':
    unittest.main()
