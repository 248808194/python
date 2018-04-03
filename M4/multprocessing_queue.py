#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Zhoutao
#create_date:2017-03-31-14:24
# Python 3.5


import multiprocessing,time,queue
q=queue.Queue()



def chef():
    count = 0
    while True:
        q.put('包子%s'%count)
        print('生产了%s个包子了'%count)
        count += 1
        time.sleep(0.1)


def consumer(name):
    while True:
        print('%s 拿到骨头，并且吃了%s' % (name, q.get()))
        time.sleep(0.5)




c = multiprocessing.Process(target=chef).start()


multiprocessing.Process(target=consumer,args=('zhoutao,',)).start()
multiprocessing.Process(target=consumer,args=('zhoutao1,',)).start()
multiprocessing.Process(target=consumer,args=('zhoutao2,',)).start()
multiprocessing.Process(target=consumer,args=('zhoutao3,',)).start()
multiprocessing.Process(target=consumer,args=('zhoutao4,',)).start()
