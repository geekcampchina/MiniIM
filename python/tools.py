hex_data = [
    0x01, 0x00, 0x00, 0x13,
    0x00, 0x03, 0x4C, 0x79, 0x75,
    0x01, 0x04, 0x61, 0x62, 0x63, 0x64,
    0x02, 0x06, 0x74, 0x65, 0x6C, 0x6E, 0x65, 0x74,
]

with open('input.frame', 'wb') as f:
    f.write(bytes(hex_data))