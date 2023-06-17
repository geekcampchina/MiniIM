import argparse
import signal
import socket

from happy_python.happy_log import HappyLogLevel

from common import hlog


__version__ = '0.0.1'


# noinspection PyUnusedLocal
def sigint_handler(sig, frame):
    hlog.info('\n\n收到 Ctrl+C 信号，退出......')
    exit(0)


def main():
    parser = argparse.ArgumentParser(prog='mini_im_client',
                                     description='迷你IM客户端',
                                     usage='%(prog)s -H|-P|-l|-m|-v')

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

    parser.add_argument('-m',
                        '--message',
                        help='（必选）消息',
                        required=True,
                        type=str,
                        action='store',
                        dest='message')

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
    message = args.message

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((host, port))

        sock.sendall(bytes(message + "\n", "utf-8"))

        received = str(sock.recv(1024), "utf-8")

    hlog.info("Sent:     {}".format(message))
    hlog.info("Received: {}".format(received))


if __name__ == "__main__":
    # 前台运行收到 CTRL+C 信号，直接退出。
    signal.signal(signal.SIGINT, sigint_handler)

    main()
