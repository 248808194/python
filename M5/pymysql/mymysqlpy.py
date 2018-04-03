#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Zhoutao
#create_date:2017-05-03-13:59
# Python 3.5

import pymysql
import time
import threading


a = time.time()
conn = pymysql.connect(host='127.0.0.1',port=3306,user='root',password='newbie',db='test')

cursor = conn.cursor()
#
list1 = []
for i in range(1000000):
    list1.append((i,i))



cursor.executemany('insert into student(name,age) VALUES (%s,%s)',list1)
conn.commit()




# tlist = []
# for i in range(len(list1)):
#     t = threading.Thread(target=excutesql,args=(list1.pop(),))
#     tlist.append(t)
#
# print(tlist)
# for i in tlist:
#     i.start()
#
# for i in tlist:
#     i.join()
#
# print(time.time()  -a )
#
