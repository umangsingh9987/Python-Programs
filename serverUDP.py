#pedux
# -*- coding: utf-8 -*-

import socket

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
ip = "0.0.0.0"
port = 888

try:
    orig = (ip, port)
    server.bind(orig)

    while True:
        msg, friend = socket.recv(1024)
        server.sendto(raw_input("Você: ") + "\n", (ip, port))
        print friend[0] + ":" + msg

    server.close()

except Exception as err:
    print "Erro: " + str(err)
    server.close()
