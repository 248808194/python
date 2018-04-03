#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Zhoutao
#create_date:2017-03-28-13:24
# Python 3.5

#select 模拟socketserver,单线程下的多路复用

import select
import socket
import queue

server = socket.socket()
server.bind(('127.0.0.1',9999,))

server.listen(1000)

server.setblocking(False) #1设置成非阻塞模式，0 就是false recv，accept 都不阻塞了，不阻塞没有连接就报错
msg_dict = {}


inputs = [server,] #3 为了让kernel检测连接需要传给kernel一个列表，有多个个连接，就全部放到input下，交给select --》 kernel 6：首次没有链接进来，先检测自己 --》server，server如果活动了就代表有人来了
outputs = [] #

while True:
    readable,writeable,exceptional = select.select(inputs,outputs,inputs) #4 传3戈参数进去，让kernel检测哪些链接，有问题也要放到inputs下去，
    #如果select 有链接进来会返回三个数据,如果链接出现异常会出现在exceptional 下，如果进来的会出现readable下
    print(readable,writeable,exceptional)
    #[server首次接受到client连接信息 readable下的数据 <socket.socket fd=3, family=AddressFamily.AF_INET, type=2049, proto=0, laddr=('127.0.0.1', 9999)>] [] []
    #fd 是文件描述符

    for r in readable:
        if r is server: #代表来了一个新连接，代表建立连接
            conn,addr = server.accept() #2 没有连接就报错，确保没有链接就不要獒走这一步
            print(conn,addr) #连接已经进来了
            inputs.append(conn)#因为新建立的连接还没发数据过来，现在就接受的话程序就报错了，所以要想实现这个客户端发数据来时server端能知道就需要让select再检测conn
            #一旦建立链接就生成一个字典
            msg_dict[conn] = queue.Queue() #初始化一个队列，存放要返回给客户端的数据
        else: #如果不是新连接直接收数据就行
            data = r.recv(1024)
            print('收到数据',data)
            msg_dict[r].put(data) #直接put数据,等到下一次循环的时候发送
            #如何做到不立即发送给客户端，可以先把发送的数据先丢到一个队列下去
            #每个连接接受的数据在发回自己的链接里
            outputs.append(r) #放入返回的连接队列




#将连接放到outputs下，下一次select的时候就可以发送过去了。
    for w in writeable: #要返回给客户端的链接列表
        data_to_client = msg_dict[w].get()
        w.send(data_to_client) #返回给客户端源数据
        outputs.remove(w)



    for e in exceptional: #链接断开或出问题了，服务器端就无需检测了，直接从exceptional下删除掉就行
        if e in outputs:
            outputs.remove(e)
        inputs.remove(e)
        del msg_dict[e]



