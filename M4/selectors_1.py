#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Zhoutao
#create_date:2017-03-28-16:26
# Python 3.5


#默认用epool，如不支持epool，
import selectors
import socket

sel = selectors.DefaultSelector()


def accept(sock, mask):
    conn, addr = sock.accept()  # Should be ready
    print('accepted', conn, 'from', addr)
    conn.setblocking(False)
    sel.register(conn, selectors.EVENT_READ, read) #新链接注册read 回调read函数


def read(conn, mask):
    data = conn.recv(1024)  # Should be ready
    if data:
        print('echoing', repr(data), 'to', conn)
        conn.send(data)  # Hope it won't block
    else:
        print('closing', conn)
        sel.unregister(conn)
        conn.close()


sock = socket.socket()
sock.bind(('localhost', 10000))
sock.listen(100)
sock.setblocking(False)
sel.register(sock, selectors.EVENT_READ, accept) #注册事件， 把sock注册到sel中去，让sel监听，accept，只要来一个新链接就调accept这个函数

while True:
    events = sel.select() #默认是阻塞，有活动链接就往下走，返回活动的链接列表
    for key, mask in events:
        callback = key.data #调用accept
        callback(key.fileobj, mask) #key.fileobj 就是socket链接
