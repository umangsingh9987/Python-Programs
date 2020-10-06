#pedux
# -*- coding: utf-8 -*-
import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    client.connect(("172.217.29.238", 80))
    client.send("GET / HTTP/1.1\nHost: google.com\n\n\n")

    pacotes_recebidos = client.recv(1024)

    print pacotes_recebidos

except:
    print "Conexão falhou"
