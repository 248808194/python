#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Zhoutao
#create_date:2017-03-17-09:48
# Python 3.5

import socket

IP_PROT = ('127.0.0.1',9999)
client = socket.socket()
client.connect(IP_PROT)


while True:
    cmd = input('enter a commond:')

    if len(cmd) == 0 or len(cmd.strip()) == 0 :continue #检查纯空格消息，和空消息
    elif cmd == 'exit':print('程序执行完毕程序退出');client.close();break
    client.sendall(cmd.encode('utf8'))
    recv_file_size = client.recv(1024).decode()
    client.sendall(b'R') #客户端发送Ｒ,告诉服务器段可以开始发送数据
    file_size = 0 #初始接受的文件大小
    recv_new_date = b'' #新建一个文件用于保存接受数据
    print(recv_file_size)
    while file_size < int(recv_file_size): #开始循环发送接受数据
        tmp_date = client.recv(1024)
        recv_new_date += tmp_date
        file_size += len(tmp_date)
    print(file_size)

    print(recv_new_date.decode())

client.close()
