import signal
import socket
import sys

from common import hlog


# noinspection PyUnusedLocal
def sigint_handler(sig, frame):
    hlog.info('\n\n收到 Ctrl+C 信号，退出......')
    exit(0)


def main():
    host, port = "localhost", 9999
    data = " ".join(sys.argv[1:])

    # Create a socket (SOCK_STREAM means a TCP socket)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        # Connect to server and send data
        sock.connect((host, port))
        sock.sendall(bytes(data + "\n", "utf-8"))

        # Receive data from the server and shut down
        received = str(sock.recv(1024), "utf-8")

    hlog.info("Sent:     {}".format(data))
    hlog.info("Received: {}".format(received))


if __name__ == "__main__":
    # 前台运行收到 CTRL+C 信号，直接退出。
    signal.signal(signal.SIGINT, sigint_handler)

    main()
