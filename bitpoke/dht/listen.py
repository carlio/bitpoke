
import socket


def listen(ip, port):
    sock = socket.socket(socket.AF_INET,
                         socket.SOCK_DGRAM)
    sock.bind((ip, port))

    while True:
        data, addr = sock.recvfrom(1024)
        print "received message:", data


if __name__ == '__main__':
    import sys
    ip = sys.argv[1]
    port = int(sys.argv[2])
    listen(ip, port)
