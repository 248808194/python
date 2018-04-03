#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Zhoutao
#create_date:2017-02-14-13:49
# Python 3.5


class Students(object):
    '''学生类'''

    def __init__(self,name,school_obj):
        self.name = name #学生姓名
        self.school_obj = school_obj #学生所属学生对象
        # print(self.school_obj)


    def register(self,money): #注册
        print(self.school_obj.SCHOOL_STUDENTS)

        if self.name in self.school_obj.SCHOOL_STUDENTS.keys():
            print('学生已经存在')
        else:
            self.school_obj.SCHOOL_STUDENTS[self.name] = money


    def chose_class(self):
        #选择当前校区已经存在的班级
        #选择好后，直接取扣款　调用扣款函数
        #扣款后直接把学生名字更新到班级的ｓｔｕｄｅｎｔｓ的列表列表中
        #  这里其实因该把扣钱独立出来，鞋一个　加钱　减钱的类，但是这里没有老师工资一说罢了
        for i in self.school_obj.SCHOOL_CLASS.keys():
            print('当前可选班级为:%s'%i)

        self.inp_cho_class = input('选择班级')
        if self.inp_cho_class in self.school_obj.SCHOOL_CLASS.keys():
            self.school_obj.SCHOOL_CLASS[self.inp_cho_class]['students'].append([self.name,None])
            # print(self.school_obj.SCHOOL_LESSON[self.inp_cho_class]['lesson_price'])
            self.school_obj.SCHOOL_STUDENTS[self.name] -= int(self.school_obj.SCHOOL_LESSON[self.school_obj.SCHOOL_CLASS[self.inp_cho_class]['lesson_name']]['lesson_perid'])
        else:
            print('课程不存在')