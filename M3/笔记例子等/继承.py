#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Zhoutao
#create_date:2017-02-06-16:50
# Python 3.5

class Person(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.sex = 'normal'
        print(self)


    def talk(self):
        print('person is talking....')


class WhitePerson(Person,object):
    pass

class BlackPerson(Person,object): #实现继承　＃　继承的关系已改是属于关系，ｅｘａｍｐｌｅ　黑人属于人这个夫类

    def __init__(self,name,age): # 重构夫类的构造函数，但是还想要夫类的构造函数 --》 先继承夫类的方法，在重构
        # Person.__init__(self,name,age,)    # 将夫类的name，age拿过来 # 有多少拿多少，同事子类的构造函数也需要把夫类全部拿过来，只多不少
        super(BlackPerson,self).__init__(name,age)
        self.sex = 'strong'                     # 修改夫类的self.sex
        self.other = 'other'
        print(self.name,self.age,self.sex)



    def talk(self): # 虽然继承了person 但是这里的talk是重写了夫类的talk 接口继承
        print('Black person name is %s, he is  talking someting'%self.name)

    def walk(self):
        print( 'Black person name is  %s, he is  walking...'%self.name)


B = BlackPerson('sb',30)
print(B)
B.walk()
B.talk()