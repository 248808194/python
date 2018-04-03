#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Zhoutao
#create_date:2017-02-06-13:48
# Python 3.5

class role(object):
    public_attr = 'public'
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex
        self.__priv = 'is priv' # 私有属性



    def get_name(self):
        print('my name is %s'%self.name)
        # print(self.__priv)


    def get_priv_from_out(self):
        return self.__priv


    def qwer(self,my_name):
        print('current name is %s'%(self.name,))
        print('change my name %s to %s' %(self.name,my_name))
        self.name = my_name
        print('after name is %s'%self.name)



person1 = role('zhoutao',22,'man')
person2 = role('zhoutao2',23,'man2')

# 定义person1的私有方法

#如何定义一个私有方法 定义一个函数
#通过实例方法复制给定义的函数

# def p1_name(self):
#     self.name = 'others'
#     print('is p1_name  %s'%self.name)
#
# person1.get_name = p1_name # 仅仅p1_name就可以了
#
# person1.get_name(person1) # 外部的话需要自己传，类内部直接写self就行
# # 这里的persion1 = self 在类中自己传，在外部的话需要自己调用
#
# person1.get_name()

#
# print(person1.get_name)
# print(person2.get_name)
# print(role.get_name)
#
# print('p1 public attr is %s'%person1.public_attr)
# print('p2 public attr is %s'%person2.public_attr)
#
# print('will change public attr')
# # role.public_attr = 'role_change_attr' # 通过类名修改共有属性
# person2.public_attr = 'role_p2_attr'
# print('after change public attr persion1 is %s persion2 is %s'%(person1.public_attr,person2.public_attr))
# print(role.public_attr)
#
# person1.qwer('zhoutao2')
# person1.get_name()
#
# a = person1.get_priv_from_out()
# print(a)
#
# print(person1._role__priv) # 强制访问私有变量
