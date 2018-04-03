#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Zhoutao
#create_date:2017-04-13-09:19
# Python 3.5



import selectors
import socket


class FtpServer(object):

    def __init__(self):
        self.sel = selectors.SelectSelector()
        self.sock = socket.socket()
        self.sock.setblocking(False)
        self.sock.bind(('127.0.0.1',9999,))
        self.sock.listen(10000)
        self.sel.register(self.sock,selectors.EVENT_READ,self.accept)

    def accept(self,sock,mask):
        conn,addr = sock.accept()
        print('accept',conn,'recv',addr)
        # conn.setblocking(False)
        self.sel.register(conn,selectors.EVENT_READ,self.read)
        self.flag = False

    def read(self,conn,mask):
        if self.flag == False:
            self.data = conn.recv(1024)
            if self.data: #每次if data 都会发
                action_dict  = eval(self.data)
                command = action_dict['action']
                if hasattr(self,command):
                    func = getattr(self,command)
                    func(conn,mask)

            else:
                print('shutdown',conn)
                self.sel.unregister(conn)
                conn.close()


    def get(self,conn,mask):
        f = open('150','rb')
        for line in f:
            try:
                conn.send(line)
            except BlockingIOError:
                print('blocked')

        f.close()
        print('file closed')


    def run(self):
        while True:
            events = self.sel.select()
            for key,mask in events:
                callback = key.data
                callback(key.fileobj,mask)

a = FtpServer()
a.run()