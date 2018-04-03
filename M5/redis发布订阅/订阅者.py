#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Zhoutao
#create_date:2017-05-02-10:59
# Python 3.5


from redishelper import RedisHelper

obj = RedisHelper()

redis_sub = obj.subscribe()

while True:
    msg = redis_sub.parse_response()
    print(msg)



    def subscribe(self): #订阅
        pub = self.__conn.pubsub()
        pub.subscribe(self.channle_sub) #从频道读取消息
        pub.parse_response()
        return pub
