#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Zhoutao
#create_date:2017-03-21-13:58
# Python 3.5

import socketserver

class MyTCPHandler(socketserver.BaseRequestHandler): #每一个客户端请求过来都会实例化这个类

    def handle(self): #handler默认在客户端里面是空的，和客户端所有的交互都是在handle完成的，每一个请求过来，都是handle处理规定的
        while True:
            self.date = self.request.recv(1024).strip()
            print('{} wrote'.format(self.client_address[0]))
            print(self.date)
            if not self.date:
                print('client is disconnected');break
            self.request.sendall(self.date.upper())


if __name__ == '__main__':
    IP_PORT = ('127.0.0.1',9999,)
    server = socketserver.ForkingTCPServer(IP_PORT,MyTCPHandler) # ip端口当做参数传入，TCPServer开始监听，没一个客户端请求进来就实例化MyTCPHandler这个类，然后拿这个实例化的TCPHandler去和客户端做交互
    server.serve_forever()