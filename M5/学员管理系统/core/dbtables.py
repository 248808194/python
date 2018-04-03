#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Zhoutao
#create_date:2017-05-17-13:18
# Python 3.5

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import  Column,Integer,String,ForeignKey,UniqueConstraint,Index,Date,Enum,Table
from sqlalchemy.orm import sessionmaker,relationship
from sqlalchemy import create_engine


engine = create_engine('mysql+pymysql://root:newbie@127.0.0.1/school_manager?charset=utf8',max_overflow=5,echo=False)

Base = declarative_base()


student_m2m_class = Table('student_m2m_class',Base.metadata,
                          Column('student.id',Integer,ForeignKey('student.id')),
                          Column('class.id',Integer,ForeignKey('class.id'))

                          )


class Techer(Base): #老师表
    __tablename__ = 'techer'
    id = Column(Integer,primary_key=True)
    name  = Column(String(64),nullable=False,unique=True)
    password = Column(String(128),nullable=False)

    # def __repr__(self):
    #     return '%s %s'%(self.name,self.password)

class Course(Base): #课程表
    __tablename__ = 'course'
    id = Column(Integer,primary_key=True)
    coursename = Column(String(64),nullable=False)


class Class(Base): # 班级表
    __tablename__ = 'class'
    id = Column(Integer,primary_key=True)
    classname  = Column(String(64),nullable=False)
    courseid = Column(Integer,ForeignKey('course.id'))
    techersid = Column(Integer,ForeignKey('techer.id'))
    courses = relationship('Course',backref='my_class',foreign_keys=[courseid])
    techers = relationship('Techer',backref = 'my_class',foreign_keys=[techersid])
    students = relationship('Student',secondary= student_m2m_class,backref ='class')






class Student(Base): #学生表
    __tablename__ = 'student'
    id = Column(Integer,primary_key=True)
    name  = Column(String(64),nullable=False)
    password = Column(String(128),nullable=False)
    qqnumber = Column(String(32))
    classs = relationship('Class',secondary= student_m2m_class,backref = 'student')

    def __repr__(self):
        return '%s'%self.id



class Study_record(Base): #上课记录表
    __tablename__ = 'studyrecord'
    id = Column(Integer,primary_key=True)
    student_id = Column(Integer,ForeignKey('student.id'))
    techer_id = Column(Integer,ForeignKey('techer.id'))
    record = Column(Enum('yes','no'),default='yes')
    day = Column(Integer)
    score = Column(String(32),nullable=False)
    homework = Column(String(64),default='no')
    class_id = Column(Integer,ForeignKey('class.id'))
    techerid = relationship('Techer',foreign_keys=[techer_id],backref='study_record')
    studentid = relationship('Student',foreign_keys=[student_id],backref='study_record')
    classid = relationship('Class',foreign_keys=[class_id],backref='study_record')


Base.metadata.create_all(engine)
#
#
# #
# Session  = sessionmaker(bind=engine)
# session = Session()
#
#
#
#
# t1 = Techer(name='t1',password='123456')
# t2 = Techer(name='t2',password='123456')
# t3 = Techer(name='t3',password='123456')
# session.add_all([t1,t2,t3])
#
#
# cou1 = Course(coursename='python')
# cou2 = Course(coursename='linux')
# cou3 = Course(coursename='go')
#
# session.add_all([cou1,cou2,cou3])
#
# c1 = Class(classname='python_1期',courses=cou1,techers=t1)
# c2 = Class(classname='Linux_1期',courses=cou2,techers=t2)
# c3 = Class(classname='Go_1期',courses=cou3,techers=t3)
#
# session.add_all([c1,c2,c3])
#
#
# #
# s1 = Student(name='s1',password='123456',qqnumber='548789')
# s2 = Student(name='s2',password='1234562',qqnumber='12548789')
# s3 = Student(name='s3',password='1234563',qqnumber='21548789')
#
# s1.classs = [c1,c2,c3]
# s2.classs = [c2,c3]
# s3.classs = [c1]
#
# session.add_all([s1,s2,s3])
# #
# r1 = Study_record(studentid=s1,techerid=t1,record='yes',day=1,score=100,classid=c1)
# r2 = Study_record(studentid=s2,techerid=t2,record='yes',day=1,score=100,classid=c1)
# r3 = Study_record(studentid=s3,techerid=t3,record='yes',day=1,score=100,classid=c2)
# #
# session.add_all([r1,r2,r3])
# session.commit()





