#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Zhoutao
#create_date:2017-01-20-14:15
# Python 3.5

import random

def create_random_code():
    '''
    随机验证码
    :return: 字母+ 数字组合
    '''
    a=[]
    for i in range(6):
        r=random.randrange(0,5)
        if r == 2 or r == 4:
            num = random.randrange(0,10)
            a.append(str(num))
        else:
            temp=random.randrange(65,91)
            c=chr(temp)
            a.append(c)

    resurt="".join(a)
    return resurt
