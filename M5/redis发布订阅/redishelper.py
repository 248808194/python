#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Zhoutao
#create_date:2017-05-02-10:58
# Python 3.5

import redis


class RedisHelper(object):
    def __init__(self):
        self.__conn = redis.Redis(host='127.0.0.1', port=6379)
        self.channle_sub = 'fm104.5' #订阅频道
        self.channle_pub = 'fm104.5' #发布频道

    def public(self, msg): #发布
        self.__conn.publish(self.channle_pub, msg) #发布一个消息到频道
        return True

    def subscribe(self): #订阅
        pub = self.__conn.pubsub()
        pub.subscribe(self.channle_sub)
        pub.parse_response()
        return pub
