#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Zhoutao
#create_date:2017-05-18-15:17
# Python 3.5
import os,sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from core.dbtables import  engine
from core.dbtables import Techer
from core.dbtables import Class
from core.dbtables import Student
from core.dbtables import Course
from core.dbtables import Study_record
from core.dbtables import student_m2m_class
from sqlalchemy.orm import  sessionmaker
from sqlalchemy import and_, or_



class Tech(object):
    def __init__(self):
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def login(self,username,password):
        obj = self.session.query(Techer).filter(and_(Techer.name == username,Techer.password==password)).first()
        self.id = obj.id
        self.username = username

        return obj


    def manager_clss(self):
        '''管理班级'''
        cls_objs = self.session.query(Class).filter(Class.techersid==self.id).all()
        print('当前执教班级如下')
        for i in cls_objs:print('ID:%s\t NAME:%s'%(i.id,i.classname))
        # chose_class = int(input('请选择班级进行管理ID:'))
        chose_class = 2
        cls = self.session.query(Class).filter(Class.id == chose_class).one()
        class_stu = cls.student
        print(class_stu)
        # input_day = int(input('输出本次上课记录（第几天）：'))
        input_day = 2
        #通过stu id class id 在ｓｔｕｄｙｒｅｃｏｒｄ中插入记录

        record_list = []
        for i in class_stu:
            i = i
            print(i,type(i))
            Study_record(studentid=i, techer_id=self.id, record='yes', day=input_day, score=100, class_id=chose_class)

        #修改分数update(stu_score)
        print('在当前班级下分配修改学员分数')
        print(class_stu)
        for i in class_stu:
            print('----')
            i=int(str(i))
            pri_id = self.session.query(Study_record).filter(Study_record.student_id == i,Study_record.day == input_day,Study_record.class_id == chose_class).first().id
            single_stu_obj = self.session.query(Study_record).filter(Study_record.id == pri_id).first()
            a = self.session.query(Student).filter(Student.id == single_stu_obj.student_id).first().name
            b = self.session.query(Class).filter(Class.id == single_stu_obj.class_id).first().classname
            c = single_stu_obj.day
            print(a,b,c)

            inp_score = input('学生：%s    在班级:%s  第%s天的成绩为:'%(a,b,c))


            # single_stu_obj.update({'score':inp_score})
            single_stu_obj.score=inp_score



        self.session.commit()








    def create_class(self):
        '''创建班级'''
        obj = (self.session.query(Class).filter().all())
        for i in obj:
            print('当前存在的班级--%s'%i.classname)
        obj_course = self.session.query(Course).filter().all()
        course_id_list = []
        for i in obj_course:
            print(i.id,i.coursename)
            course_id_list.append(i.id)

        course = int(input('请选择课程:'))
        if course in course_id_list:
            str_classname = input("输入新开班名称:")
            print(str_classname)
            new_class = Class(classname=str_classname,courseid=course,techersid=self.id)
            self.session.add_all([new_class])
            self.session.commit()
        else:
            print('输入错误')
        print('开始添加学员')
        #打印出所有学员
        #批量添加学员
        obj_stu  = self.session.query(Student).filter().all()
        # print(obj_stu.id,obj_stu.name,obj_stu.qqnumber)
        tmp_qqnumber_list = []
        for i in obj_stu:
            print('学员ID:%s\t学员姓名:%s\t学员QQ号:%s"'%(i.id,i.name,i.qqnumber))
            tmp_qqnumber_list.append(i.qqnumber)

        print('添加学员ＱＱ号将学员批量加入到班级')
        new_class_qqnumber_list = ''.join(input('输入学员ＱＱ用逗号分割').strip().split()).split(',') #过滤空格
        class_id = self.session.query(Class).filter(Class.classname==str_classname).one().id
        class_obj = self.session.query(Class).filter(Class.id==class_id).first()
        stu_list = []
        for i in new_class_qqnumber_list:
            c_obj = self.session.query(Student).filter(Student.qqnumber==i).first()
            stu_list.append(c_obj.name)
            c_obj.classs.append(class_obj)
        self.session.commit()

        print('''
        新开班-%s
        所学课程-%s
        任课老师-%s
        当前班级学生-%s
        '''%(str_classname,self.session.query(Course).filter(Course.id==course).first().coursename,self.username,stu_list)
              )











        pass

    def manager_stu(self):
        '''管理学员'''
        pass


    def msg(self):
        msg_dict = {
            1:'管理班级',
            2:'创建班级',
            3:'管理学员'
        }
        msg_dict_self = {1:'manager_clss',2:'create_class',3:'manager_stu'}
        for k,v in msg_dict.items():
            print(k,'\t-----\t',v)
        func_str = int(input('请选择功能:'))
        if hasattr(self,msg_dict_self[func_str]):
            func = getattr(self,msg_dict_self[func_str])
            func()



# obj = Tech()
# obj.login('t2','123456')
# obj.manager_clss()