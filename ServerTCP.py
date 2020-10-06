#pedux
# -*- coding: utf-8 -*-

import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip = "0.0.0.0"
port = 888
file = open("shell.php", "w")

try:
    server.bind((ip, port))
    server.listen(5)
    print "Listening: " + ip + ":" + str(port)

    (client_socket, address) = server.accept()

    print "Received from: " + address[0]

    data = client_socket.recv(1024)
    file.write(data)

    server.close()

except Exception as err:
    print "Erro: " + str(err)
    server.close()
