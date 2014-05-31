import socket
import os
from bitpoke.dht import make_node_id
from bitpoke.bencoding import encode, decode


def _send(message, ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(message, (ip, port))


def ping():
    data = {
        'y': 'q',
        'q': 'ping',
        'a': {
            'id': os.urandom(20)
        },
        't': '1',
    }
    data = encode(data)
    return data


def find_nodes(my_ip, my_port, query_ip, query_port):
    my_node_id = make_node_id(my_ip, my_port)
    dest_node_id = 'abcdefghijklmnopqrstuvwxyz'
    dest_node_id = my_node_id
    data = {
        't': '1',
        'y': 'q',
        'q': 'find_nodes',
        'a': {
           'id': my_node_id,
           'target': dest_node_id,
        }
    }
    data = encode(data)
    return data


if __name__ == '__main__':
    #data = find_nodes('188.226.250.164', 6881, '188.226.250.164', 6881)

    data = ping()

    print data
    _send(data, '67.215.242.139', 6881)


