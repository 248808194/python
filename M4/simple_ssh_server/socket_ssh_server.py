#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Zhoutao
#create_date:2017-03-17-09:48
# Python 3.5


import socket,os

IP_PROT = ('127.0.0.1',9999)
server =socket.socket()
server.bind(IP_PROT)
server.listen()


while True:
    print('first while')
    conn,addr = server.accept() #每进来一个链接就生成一个addr
    print('new conn:',conn,addr)
    while True:
        print('next while')
        date = conn.recv(1024)
        if not date:print("client is disconnected");break #检查客户端是否断开如果断开的话跳出循环建立下一个conn,addr 提供给下一个来访的客户端链接
        print('excute commond date')
        cmd_res = os.popen(date.decode()).read()
        if len(cmd_res) == 0:cmd_res = 'worng cmd' #如果是假命令主动制造一个命令返回给客户端，防止客户端阻塞
        conn.sendall( str( len( cmd_res.encode() ) ).encode() ) #先发发送的数据的总大小发送给客户端,#这里需要２次转码以保证有中文的情况下数据的完整性
        print(len(cmd_res))
        conn.recv(1024) #接受一个消息起到杜绝粘包，
        # if recv_ready == 'R':

        conn.sendall(cmd_res.encode()) #当服务器接受到关键字Ｒ之后。开始正式发送数据


server.close()