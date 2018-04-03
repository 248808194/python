#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Zhoutao
#create_date:2017-05-18-15:17
# Python 3.5
import os,sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from core.dbtables import  engine
from core.dbtables import  Student
from core.dbtables import  Class
from core.dbtables import  Study_record
from sqlalchemy.orm import  sessionmaker
from  sqlalchemy import func
from sqlalchemy import and_, or_


class Stu(object):

    def __init__(self):
        Session = sessionmaker(bind=engine)
        self.session = Session()


    def login(self,username,password):

        obj = self.session.query(Student).filter(and_(Student.name == username,Student.password==password)).first()
        self.id = obj.id
        self.name = obj.name
        print(self.id,self.name)
        self.chose_class()


    #打印出学生所在的所有班级让学生选择
    def chose_class(self):
        obj_c = self.session.query(Student).filter(Student.id==self.id).first()
        print(obj_c)
        for i in obj_c.classs:
            print('当前班级:%s\t班级ID：%s'%(i.classname,i.id))

        self.choseid = input('请输入班级ID：')
        self.msg()
    def update_corse(self):
        obj_no_home_work = self.session.query(Study_record).filter(Study_record.student_id == self.id,Study_record.class_id == self.choseid,Study_record.homework == 'no').all()
        if  obj_no_home_work:
            for i in obj_no_home_work:
                print('未提交的作业day：%s,记录ID:%s'%(i.day,i.id))
            update_cor = input('选择提交作业记录ID：')
            self.session.query(Study_record).filter(Study_record.id==update_cor).update({'homework':'yes'})
            self.session.commit()
        else:
            print('学生作业已经全部提交')

    def check_couse(self):
        asdf = self.session.query(Study_record).filter(Study_record.id == self.id,Study_record.class_id==self.choseid,Study_record.homework=='yes').all()
        for i in asdf:
            print('当前天数:%s  成绩:%s'%(i.day,i.score))

    def check_rack(self):
        '''查看排名'''
        abc = self.session.query(Class).filter(Class.id ==self.choseid).first()
        print(abc)
        rack_dict = {}

        for i in abc.students:
            print(i.name)
            abb = self.session.query(func.sum(Study_record.score)).filter(Study_record.student_id ==i.id,Study_record.class_id == self.choseid).scalar()
            rack_dict[i.name] = abb

        print(rack_dict)
        all_stu_count = len(rack_dict.values())
        my_abb = rack_dict[self.name]
        print(my_abb)
        for i in rack_dict.values():
            if my_abb < i:
                all_stu_count += 1

        print('我的班级排名',all_stu_count)


    def msg(self):
        print('''
        当前班级ID：%s
        1:提交作业
        2：查看成绩
        3：查看班级排名
        '''%(self.choseid))
        chose_select = input("请选择操作")
        if chose_select == '1':
            self.update_corse()
        elif chose_select == '2':
            self.check_couse()
        elif chose_select == '3':
            self.check_couse()
        else:
            print('worng input ')




A=Stu()
A.login('s1',123456)
A.check_rack()