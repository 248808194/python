#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Zhoutao
#create_date:2017-04-19-14:56
# Python 3.5

#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Zhoutao
#create_date:2017-03-31-13:29
# Python 3.5


import threading,time

cond = threading.Condition()

def hider():
    print('step 1：先睡觉1秒确保seeker中的方法先运行')
    time.sleep(1)
    cond.acquire() # 上锁
    print('我已经把眼睛蒙上了') #打印我已经藏好了
    cond.notify() #通知seeker a
    cond.wait() #阻赛等待
    print('find you') #有了通知就不阻赛打印findyou  b
    cond.notify() #发送一个通知给seeker的bb不要阻赛了
    cond.release()

def seeker():
    cond.acquire() #上锁
    cond.wait() #阻赛等待
    print('我已经藏好了') #接受到hider a
    cond.notify() #发送一个通知 b
    cond.wait() #发送通知b 之后马上阻赛等待 bb
    cond.release() #结束，释放锁
    print('呵呵，被你找到了')
    print('6 done')


h = threading.Thread(target=hider)
s = threading.Thread(target=seeker)

h.start()
s.start()



#example 2 condition版的生产者消费者模型


import threading,time
count = 1000
cond = threading.Condition()

def producer():
    global count
    while True:
        cond.acquire()
        if count > 1000:
            cond.wait()
        else:
            count += 100
            print('开始生产100个包子当前总包子为%s'%count)
            cond.notify()
            cond.release()
            time.sleep(1)


def consumer():
    global count
    while True:
        cond.acquire()
        if count < 100:
            print('包子库存已经少于100，停卖')
        else:
            count -= 2
            print('剩余包子为',count)
            cond.notify()
        cond.release()
        time.sleep(0.1)

threading.Thread(target=producer).start()
threading.Thread(target=consumer).start()