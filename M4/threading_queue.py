#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Zhoutao
#create_date:2017-03-31-14:24
# Python 3.5

#
# import threading,time,queue
#
# q=queue.Queue()
#
# #生产者

# def producer ():
#     count  = 0
#     while True:
#         q.put('骨头%s'%count)
#         print("已经生产了%s个骨头"%count)
#         count +=1
#         time.sleep(0.1)
#
#
# def consumer(name):
#     while True:
#         print('%s 拿到骨头，并且吃了%s'%(name,q.get()))
#         time.sleep(0.5)
#
#
# p = threading.Thread(target=producer)
# p.start()
#
# c = threading.Thread(target=consumer,args=('zhoutao',))
# c1 = threading.Thread(target=consumer,args=('zhoutao1',))
# c2 = threading.Thread(target=consumer,args=('zhoutao2',))
# c.start()
# c1.start()
# c2.start()
import threading,time,queue

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
        time.sleep(1)




c = threading.Thread(target=chef).start()


threading.Thread(target=consumer,args=('zhoutao,',)).start()
threading.Thread(target=consumer,args=('zhoutao1,',)).start()
threading.Thread(target=consumer,args=('zhoutao2,',)).start()
threading.Thread(target=consumer,args=('zhoutao3,',)).start()
threading.Thread(target=consumer,args=('zhoutao4,',)).start()
