#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Zhoutao
#create_date:2017-02-14-13:49
# Python 3.5

import pickle
from conf import settings

class Techer(object): #老师类
    def __init__(self, name):
        self.tech_name = name
    '''
　通过ｔｅｃｈｅｒ名字去查看校区实例下是否存在该老师
如果存在，让用户选择操作
通过关联校区实例去查看学生列表，分数，选择上课班级等等方法
    '''

    def check_name_in_school(self): #查看老师在那所分校
        for k,v in settings.school.items():
            with open(v,'rb') as f:
                school_obj = pickle.load(f)
                if self.tech_name in school_obj.SCHOOL_TECHER: #分校中找到教师就跳出循环 return 出实例化的对象　＃这里其实有ｂｕｇ　同一个老师也可以存在多个分校，
                    return school_obj,v


    def check_stu_list(self,school_obj): #查看学生列表
        # school_obj.SCHOOL_CLASS = {'c123': {'techername': 'techer_cc', 'lesson_name': 'linux', 'students': [ ['zhoutao',88],['xiaowang',90],['xiaoming',95] ] }}
        for i in school_obj.SCHOOL_CLASS.values():
            if i['techername'] == self.tech_name:
                for ii in i['students']:
                    print('学生姓名:%s ,学生成绩:%s'%(ii[0],ii[1]))


    def change_stu_score(self,school_obj,*arg): #修改学生分数
        # school_obj.SCHOOL_CLASS = {'c123': {'techername': 'techer_cc', 'lesson_name': 'linux','students': [['zhoutao', 88], ['xiaowang', 90], ['xiaoming', 95]]}}
        for i in school_obj.SCHOOL_CLASS.values():
            for ii in i['students']:
                if ii[0] == arg[0]:
                    old_score = ii[1]
                    ii[1] = arg[1]
                    print('学生%s 原成绩%s　成绩修改为%s' % (arg[0], old_score,arg[1]))
                    print(school_obj.SCHOOL_CLASS)


    def chose_class(self,school_obj):# 管理班级方法
        for i in school_obj.SCHOOL_CLASS.values():
            if self.tech_name  == i['techername']:
                print('选定班级为%s 进行管理'%i)