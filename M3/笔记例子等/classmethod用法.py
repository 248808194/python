#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Zhoutao
#create_date:2017-02-10-15:30
# Python 3.5

class Try_Classmethod(object):

    name = 'class_global_name'

    def __init__(self,name):
        self.name = name

    @classmethod
    def user_classmethod(self):
        print(123,self.name)


obj = Try_Classmethod('zhoutao') # classmethod方法只能调用类的全局变量，这里打印的self.name 其实就是一开始复制的 name = 'class_global_name'
obj.user_classmethod()

