#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Zhoutao
#create_date:2017-02-07-13:12
# Python 3.5

class SchoolMember(object): # 这里基类中的方法，字段，子类中都需要用　ｅｘａｍｐｌｅ　性别，年龄，姓名，都需要注册，都需要告知信息
    member = 0 # 成员计数器
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex
        self.enroll()
        print(self.member)


    def enroll(self): # enroll 注册方法
        # 每次注册成功后成员数量加１
        print("just enrolled a new school member [%s]"%self.name)
        # self.member +=1 #  这里不能用self.member ｓｅｌｆ是自己的实例，因该是基类的实例+1才行
        SchoolMember.member +=1

    def tell(self): # 打印自己的个人信息
        print(self.__dict__)
        for k,v in self.__dict__.items():
            print(
                '-----------info------------',
                k,'<---->',v
            )

    def __del__(self):
        print("fire %s "%self.name) # 程序整体结束才会自动执行稀构函数，所有　最后才是开出了s1,s2,t1
        SchoolMember.member -= 1


class Tech(SchoolMember):
    '''教师'''
    def __init__(self,name,age,sex,salary,course): # salary:课程　course：工资
        SchoolMember.__init__(self,name,age,sex)
        self.salay = salary
        self.couse = course
        # self.enroll() #调用基类的注册方法，自动注册，自动基数

    def teching(self): # 教师教课内容
        print('techer %s is teaching %s'%self.name,self.couse)


class Student(SchoolMember):
    def __init__(self,name,age,sex,course,tuition,): # tuition:学费　
        SchoolMember.__init__(self,name,sex,age)  # 经典类
        super(Student,self).__init__(name,age,sex) # 新式类
        self.course = course
        self.tuition = tuition
        self.amount = 0 # 初始化的学费
        # self.enroll() # 注册，发现教师，学生都需要注册，为了去重复代码将enroll注册方法直接放入到基类的构造函数中

    def pay_tution(self,amount):
        print('student %s has just paied %s'%(self.name,amount))
        self.amount += amount # 交的学费，看能报了很多课程



t1 = Tech('t1',30,'F','python',10000)
s1 = Student('s1',20,'F','python',11000)
s2 = Student('s2',30,'F','python',12000)
# print(s1.__dict__)
# s1.tell()
# print(s1.__dict__)
# s1.pay_tution(10000)
s1.tell()
# print(SchoolMember.member)