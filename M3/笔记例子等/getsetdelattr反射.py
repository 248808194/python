#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Zhoutao
#create_date:2017-02-13-09:18
# Python 3.5

class GET_SET_HAS_ATTR(object):

    def get_func(self):
        print('get_func')
        return 123


obj = GET_SET_HAS_ATTR()


hasattr(obj,'get_func')
a = getattr(obj,'get_func')
b = a()
print(b)


