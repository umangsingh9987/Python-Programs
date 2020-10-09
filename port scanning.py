#Pedux
# -*- coding: utf-8 -*-
import socket

ip = raw_input("Digite o IP ou endereço: ")
ports = range(65535)

for port in ports:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.settimeout(0.1)
    code = client.connect_ex((ip, port))
    if code == 0:
        print "A porta " + str(port) + " está aberta."
    else:
        print "A porta " + str(port) + " está fechada."

print "Scan finalizado."
