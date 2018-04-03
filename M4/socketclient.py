#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Zhoutao
#create_date:2017-03-28-15:37
# Python 3.5

import socket

client = socket.socket()
IP_ADDR = ('127.0.0.1',9999)
client.connect(IP_ADDR)

while True:
    msg = bytes(input(':>>'),encoding='utf8')
    client.sendall(msg)
    data = client.recv(1024)
    print(data)



client.close()