import random
import os

key = os.urandom(20)


def make_node_id(ip, port):
    ip_bytes = map(int, ip.split('.'))
    port_bytes = [(port >> 8) & 0xff, port & 0xff]
    return ''.join(map(chr, key + ip_bytes + port_bytes))


if __name__ == '__main__':
    print make_node_id('127.0.0.1', 6881)
