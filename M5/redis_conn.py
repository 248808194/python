#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Zhoutao
#create_date:2017-04-27-13:19
# Python 3.5

import redis

pool = redis.ConnectionPool(host='127.0.0.1',port=6379) #建立池，



r = redis.Redis(connection_pool=pool)
r.sadd('s1',1,2,3)
print(r.smembers('s1'))
print(r.sismember('s1',4))

