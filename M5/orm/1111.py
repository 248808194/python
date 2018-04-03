#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Zhoutao
#create_date:2017-05-09-10:43
# Python 3.5


from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import  Column,Integer,String,ForeignKey,UniqueConstraint,Index,Date,Enum
from sqlalchemy.orm import sessionmaker,relationship
from sqlalchemy import create_engine

engine = create_engine('mysql+pymysql://root:newbie@127.0.0.1/sqlalchemy_study',max_overflow=5,echo=False)

Base = declarative_base()

class Student(Base):

    __tablename__ = 'student'
    id = Column(Integer,primary_key=True,autoincrement=True)
    name = Column(String(32),unique=True,nullable=False)
    register_date = Column(String(32),nullable=False)

    def __repr__(self):
        return  '<%s -- %s>'%(self.id,self.name)


class Study_record(Base):

    __tablename__ = 'study_record'
    id = Column(Integer,primary_key=True,autoincrement=True)
    day = Column(Integer,nullable=False)
    status = Column(Enum('YES','NO'),nullable=False,) #枚举
    stu_id = Column(Integer,ForeignKey('student.id')) # 外键关联 student.id

    #relationship与mysql没有关系，只是在两个对象里面来回调用查找
    student = relationship('Student',backref='my_study_record') # 在study_record表里通过student字段查询student表的内容；backref='my_study_record'表示在student表里面通过my_study_record反查study_record表里面的内容

    def __repr__(self):
        return  '<student:%s day:%s status:%s>'%(self.student.name,self.day,self.status)



Base.metadata.create_all(engine)



Session = sessionmaker(bind=engine)
session = Session()
#
# stu_list = [
#     Student(name='zt0',register_date = '2015-05-01'),
#     Student(name='zt1',register_date = '2016-05-01'),
#     Student(name='zt2',register_date = '2015-05-01'),
#     Student(name='zt3',register_date = '2018-05-01'),
#     Student(name='zt4',register_date = '2019-05-01'),
# ]
#
# record_list =[
#     Study_record(day=1, status='YES', stu_id=1),
#     Study_record(day=2, status='NO',  stu_id=1),
#     Study_record(day=3, status='YES', stu_id=1),
#     Study_record(day=1, status='YES', stu_id=1),
# ]

# session.add_all(stu_list)
# session.commit()
# session.add_all(record_list)
# session.commit()
#
#
# session.commit()
# 查询zt0 一共上了几节课
stu_obj = session.query(Student).filter(Student.name=='zt0').first() #查询zt0 一共上了几节课 通过relationship去连表查询
stu_obj1 = session.query(Student).filter(Student.name=='zt0').first() #查询zt0 一共上了几节课 通过relationship去连表查询


print(stu_obj1.my_study_record)
print(stu_obj.my_study_record)
