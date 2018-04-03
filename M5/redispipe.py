#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Zhoutao
#create_date:2017-05-02-09:57
# Python 3.5

import redis
import time

pool = redis.ConnectionPool(host='127.0.0.1',port=6379,db=5)
r= redis.Redis(connection_pool=pool)

pipe = r.pipeline(transaction=True)

pipe.set('name','zhoutao')

pipe.set('role','role1')
pipe.execute()

