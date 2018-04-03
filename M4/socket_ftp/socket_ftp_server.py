#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Zhoutao
#create_date:2017-03-20-15:02
# Python 3.5


import socket,os,hashlib


server = socket.socket()
IP_PORT = ('127.0.0.1',9999)
server.bind(IP_PORT)
server.listen()

while True:
    conn,addr = server.accept()
    print('wait for client command')
    while True:
        date = conn.recv(1024)
        if not date:print('client is disconnected');break
        action_list = date.decode().split()
        filename =  action_list[1]
        if os.path.isfile(filename): # if has file
            m = hashlib.md5()
            file_total_size = os.path.getsize(filename)
            conn.sendall(str(file_total_size).encode())
            conn.recv(1024) #recv R
            with open(filename,'rb') as f:

                for line in f:
                    m.update(line)
                    conn.sendall(line)

                file_old_md5 = m.hexdigest()
                conn.sendall(str(file_old_md5).encode())
                print('file send done')





