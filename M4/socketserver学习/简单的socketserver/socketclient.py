#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Zhoutao
#create_date:2017-03-21-14:19
# Python 3.5


import socket

client = socket.socket()
IP_PORT = ('127.0.0.1',9999)
client.connect(IP_PORT)


while True:
    messages = 'abcdefg'
    if len(messages) == '0':continue
    client.sendall(messages.encode())
    recv_date = client.recv(1024)
    print(recv_date.decode())

