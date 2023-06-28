from common import hlog
from miniim.protocol import MiniIMField
from util import to_int


class MiniIMFieldsHandler:
    MIN_LEN = 2

    def slice_payload(self) -> bytes:
        pass

    @staticmethod
    def has_data(remain_bb: bytes, need_len: int) -> bool:
        return len(remain_bb) >= need_len

    def slice_data(self, data: bytes, step: int) -> bytes | None:
        if step == 0:
            return bytes([])

        if self.has_data(data, step):
            begin = 0
            end = step
            return data[begin: end]

        return None

    def slice_field(self, remain_bb: bytes) -> bytes | None:
        fname = 'MiniIMFieldsHandler.slice_field'
        hlog.enter_func(fname)

        hlog.input('remain_bb', remain_bb)

        if len(remain_bb) < self.MIN_LEN:
            hlog.output('result', None)
            hlog.exit_func(fname)
            return None

        value_len_bb = self.slice_data(remain_bb[1:], 1)
        hlog.var('value_len_bb', value_len_bb)

        if value_len_bb is None:
            hlog.output('result', None)
            hlog.exit_func(fname)
            return None

        value_len = to_int(value_len_bb)
        hlog.var('value_len', value_len)

        result = self.slice_data(remain_bb[0:], 2 + value_len)

        hlog.output('result', result)
        hlog.exit_func(fname)

        return result

    def run(self, remain_bb: bytes, result: list) -> None:
        fname = 'MiniIMFieldsHandler.run'
        hlog.enter_func(fname)

        hlog.input('remain_bb', remain_bb)
        hlog.input('result', result)

        field_bb = self.slice_field(remain_bb)
        hlog.var('field_bb', field_bb)

        if field_bb is None:
            hlog.exit_func(fname)
            return

        field = MiniIMField(ftype=field_bb[0], flen=field_bb[1], fvalue=field_bb[2:])
        hlog.var('field', field)

        result.append(field)

        hlog.exit_func(fname)

        index = len(field_bb) - 1
        self.run(remain_bb[index + 1:], result)
