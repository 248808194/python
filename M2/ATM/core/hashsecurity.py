#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Zhoutao
#create_date:2017-01-20-13:35
# Python 3.5

import hashlib

def hashsecurity(strsec):
    '''
    密码加密函数
    自定义一个hashlib
    传入strsec密码字符串进行加密
    :param strsec:
    :return: a
    '''
    obj = hashlib.md5(bytes('doublesec',encoding='utf8'))
    obj.update(bytes(strsec,encoding='utf8'))
    a = obj.hexdigest() #密码加密后的字符串
    return a
