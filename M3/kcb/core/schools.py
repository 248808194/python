#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Zhoutao
#create_date:2017-02-14-13:48
# Python 3.5

#最先让你选择校区，然后在校区中进行各种视图操作

import os,sys,time,datetime,pickle,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from conf import  settings
from core.lessons import  Lesson


class School(object):
    '''
    班级字典example
    拼字典
    example
    {'NAME,LINUXS1':  # 班级姓名
        {
            'TECHERNAME': 'TECHERNAME',  # 老师姓名
            'LESSON_NAME': 'LESSON_NAME',  # 课程名
            'STUDENTS': ['stu1', 'stu2', '.........'],  # 学生列表
        }
    }
    '''
    def __init__(self):
        # self.SCHOOL_NAME = None
        self.SCHOOL_STUDENTS = {} #存放学生　＋　学费　{stuname:120000}
        self.SCHOOL_TECHER = [] #存放教师
        self.SCHOOL_LESSON = {} #存放课程
        self.SCHOOL_CLASS = {} #存放班级

    def create_lesson(self): #创建课程方法
        self.lesson_name = input("课程名:")
        self.lesson_price = input('课程价格:')
        self.lesson_perid = input('课程周期:')
        lesson_obj = Lesson(self.lesson_name,self.lesson_perid,self.lesson_price)
        self.SCHOOL_LESSON[lesson_obj.lesson_name] = lesson_obj.__dict__


    def create_class(self): #创建班级方法
        self.class_name = input("您要创建的班级名称:")
        while True:
            for i in self.SCHOOL_LESSON.keys():
                print('课程如下%s'%i)
            self.class_lesson_name = input("班级关联课程:")
            if  self.class_lesson_name not in self.SCHOOL_LESSON.keys():
                print('课程未找到，请确认课程是否存在')
                continue
            else:
                print('班级:%s 成功关联课程内容%s'%(self.class_name,self.class_lesson_name))

                # 关联讲师 先打印出学校讲师，在去关联讲师，如果没有讲师则说明没讲师，无法关联，
                if not self.SCHOOL_TECHER:
                    print('有问题，学校没有老师，您先招工')
                    break
                else:
                    while True: #判断是否存在该老师ｉｄ
                        print('当前学校老师如下')
                        print(self.SCHOOL_TECHER)
                        tech_all_id = []
                        for index,name in enumerate(self.SCHOOL_TECHER):
                            print('techer_id:\t%s techer_name:\t%s'%(index,name))
                            tech_all_id.append(str(index))
                        inp_techer_id = input("请输入老师工号ID：")
                        if inp_techer_id  in tech_all_id:
                            self.techer_name = self.SCHOOL_TECHER[int(inp_techer_id)]
                            break
                        else:
                            print('tech id not found')
                            continue
            break


        self.SCHOOL_CLASS[self.class_name ] = {'techername':self.techer_name,'lesson_name':self.class_lesson_name,'students':[]} #拼接班级字典
        print(self.SCHOOL_CLASS)


    def create_techer(self): #创建老师方法
        techer_name = input('添加老师，请输入老师姓名:')
        if techer_name in self.SCHOOL_TECHER:
            print('教师存在，请从新添加')
        else:
            # techer_obj = Techer(techer_name)
            self.SCHOOL_TECHER.append(techer_name)


