#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Zhoutao
#create_date:2017-02-10-15:21
# Python 3.5


class Trystaticmethod(object):

    def __init__(self,name):
        self.name = name
        self.sex = 'F'

    @staticmethod
    def out_class_func(sex_1):
        print(sex_1.name)
        print('123')



ojb = Trystaticmethod('zhoutao')

Trystaticmethod.out_class_func(ojb) # staticmethod只是把函数写在类里面，其实和类没关系,也不能访问类中的任何属性或者方法
#如果实在要访问只能把类实例化后传入减去，