import argparse
import signal
import socketserver

from happy_python.happy_log import HappyLogLevel

from common import hlog

__version__ = '0.0.1'

from miniim import LoginMessage

from miniim.protocol import MiniIMDecoder


# noinspection PyUnusedLocal
def sigint_handler(sig, frame):
    hlog.info('\n\n收到 Ctrl+C 信号，退出......')
    exit(0)


class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        recv_data = self.request.recv(1024).strip()
        hlog.debug("{} wrote:".format(self.client_address[0]))
        hlog.trace(recv_data)

        decoder = MiniIMDecoder(recv_data)
        frame = decoder.run()

        lm = LoginMessage(user=frame.payload[0].fvalue.decode('UTF-8'),
                          password=frame.payload[1].fvalue.decode('UTF-8'),
                          client=frame.payload[2].fvalue.decode('UTF-8'))

        self.request.sendall(bytes(lm.asjson(), encoding='UTF-8'))


def main():
    parser = argparse.ArgumentParser(prog='mini_im_server',
                                     description='迷你IM服务端',
                                     usage='%(prog)s -H|-P|-l|-v')

    parser.add_argument('-H',
                        '--host',
                        help='（可选）服务端地址，默认值：localhost',
                        required=False,
                        type=str,
                        action='store',
                        default='localhost',
                        dest='host')

    parser.add_argument('-P',
                        '--port',
                        help='（可选）服务端端口，默认值：9999',
                        required=False,
                        type=int,
                        action='store',
                        default='9999',
                        dest='port')

    parser.add_argument('-l',
                        '--log-level',
                        help='（可选）日志级别，0（CRITICAL）|1（ERROR）|2（WARNING）|3（INFO）|4（DEBUG）|5（TRACE），默认值：3',
                        type=int,
                        choices=HappyLogLevel.get_list(),
                        default=HappyLogLevel.INFO.value,
                        required=False,
                        dest='log_level')

    parser.add_argument('-v',
                        '--version',
                        help='显示版本信息',
                        action='version',
                        version='%(prog)s/v' + __version__)

    args = parser.parse_args()

    hlog.set_level(args.log_level)

    host, port = args.host, args.port

    server = socketserver.TCPServer(server_address=(host, port),
                                    RequestHandlerClass=MyTCPHandler,
                                    bind_and_activate=False)

    hlog.info('服务端监听->\t%s:%s' % (host, port))

    # 设置socket参数
    server.allow_reuse_address = True
    server.allow_reuse_port = True

    # 在没有设置socket参数前，不能监听端口
    server.server_bind()
    server.server_activate()

    server.serve_forever()


if __name__ == "__main__":
    # 前台运行收到 CTRL+C 信号，直接退出。
    signal.signal(signal.SIGINT, sigint_handler)

    main()
