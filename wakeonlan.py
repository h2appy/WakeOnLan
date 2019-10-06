#!/usr/bin/env python

import socket
import sys
import codecs


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print('''Usage: wakeonlan.py <ADR> <MAC>
             (example: 192.168.11.255 00:11:32:AF:A2:13)''')
        sys.exit(1)

    # subnet broadcast address, for example 192.168.1.255
    ip = sys.argv[1]
    # MAC of the machine to be woken up
    mac = sys.argv[2]

    data = ''.join(['FF' * 6, mac.replace(':', '') * 16])
    data = codecs.decode(data, 'hex')

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    sock.sendto(data, (ip, 9))
