from dataclasses import dataclass


@dataclass
class MiniIMField:
    ftype: int
    flen: int
    fvalue: bytes
