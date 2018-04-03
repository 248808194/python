#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Zhoutao
#create_date:2017-02-10-09:24
# Python 3.5

class Test(object):

    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex
        print(self.age,self.name,self.sex)

    def __new__(cls, *args, **kwargs):  # 先执行__new__这里还没有实例化这个类，
        print("创建实例的时候先执行__new__方法,而且必须要有ｒｅｔｕｒｎ")
        return object.__new__(cls,) # 所有需要继承父亲的__new__方法,此处的cls就是类本身－－－》　Ｔｅｓｔ



A=Test(1,2,3)