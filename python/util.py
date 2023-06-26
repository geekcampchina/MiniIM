def to_hex_string(bb: bytes):
    return bb.hex(sep=' ').upper()


def to_hex(byte: int):
    return '0x%0.2X' % byte


def to_int(bb: bytes) -> int:
    return int.from_bytes(bb, byteorder='big')