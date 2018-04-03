#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Zhoutao
#create_date:2017-03-20-15:03
# Python 3.5

import socket,os,hashlib


client = socket.socket()
IP_PORT = ('127.0.0.1',9999)
client.connect(IP_PORT)



while True:
    cmd = input('>>:')
    client.sendall(cmd.encode())
    recv_file_size = int(client.recv(1024).decode())
    file_new_size = 0
    client.sendall(b'R')
    filename = cmd.split()[1]

    with open(filename+'.new','wb')as f:
        m = hashlib.md5()

        while file_new_size < recv_file_size:

            if recv_file_size - file_new_size > 1024:
                size = 1024
            else:
                size = recv_file_size - file_new_size

            date = client.recv(size)
            m.update(date)
            file_new_size += len(date)
            f.write(date)

        else:
            new_file_md5 = m.hexdigest()
            server_file_md5 =client.recv(1024)
            print(server_file_md5)
            print(new_file_md5)




