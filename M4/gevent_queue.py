#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Zhoutao
#create_date:2017-03-31-13:49
# Python 3.5

import gevent,random
from gevent.queue import Queue

tasks = Queue()

def worker(n):
    while not tasks.empty(): #如果队列不为空，那我就get数据
        task = tasks.get()
        print('worker %s got task %s'%(n,task))
        gevent.sleep(0.1)

import threading
def boss():
    i = 0
    while i < 100:
        # print(threading.current_thread())
        tasks.put_nowait(random.randint(1,100))
        # print(random.randint(1,100))
        # print(tasks)
        i+=1
    print(tasks.qsize())
    # for i in range(2001):
    #     tasks.put_nowait(i)

gevent.spawn(boss).join() #允许boss函数，并且阻赛住

print(tasks.qsize())
gevent.joinall(
    [
        gevent.spawn(worker,'zhoutao'),
        gevent.spawn(worker,'zt'),
        gevent.spawn(worker,'zhoutao1'),
        gevent.spawn(worker,'zhoutao2'),
        gevent.spawn(worker,'zhoutao3'),
    ]
)

