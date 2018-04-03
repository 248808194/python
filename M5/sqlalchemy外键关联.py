#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Zhoutao
#create_date:2017-05-15-14:17
# Python 3.5


from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import  Column,Integer,String,ForeignKey,UniqueConstraint,Index,Date,Enum,Table
from sqlalchemy.orm import sessionmaker,relationship
from sqlalchemy import create_engine
from sqlalchemy_utils import ChoiceType,PasswordType # 插件需要安装

engine = create_engine('mysql+pymysql://root:newbie@127.0.0.1/test',max_overflow=5,echo=False)

Base = declarative_base()


#两个表之间的外键关联.

#记录学生每天上课的内容，以及是否出勤


class Student(Base):

    __tablename__ = 'student'
    id = Column(Integer,primary_key=True,autoincrement=True)
    name = Column(String(64),unique=True)

    def __repr__(self):
        return "<name:%s>"%self.name

class StudyRecord(Base):
    __tablename__ = 'studyrecord'
    id = Column(Integer,primary_key=True,autoincrement=True)
    day = Column(Integer,nullable=False)
    status = Column(Enum('YES','NO'),default='YES')
    stu_id = Column(Integer,ForeignKey('student.id'))
    student = relationship('Student',backref='my_study_record') # 建立一个映射关系在studyrecord表中通过student查stuendt表的内容，在ｓｔｕｄｅｎｔ表中通过　my_study_record反查studyrecord表的内容
    # relationship不存在与数据库中，是通过ｐｙｔｈｏｎ类去查的

    def __repr__(self):
        return '<id:%s  day:%s  status:%s   stu_id:%s>'%(self.id,self.day,self.status,self.stu_id)

Base.metadata.create_all(engine)


Session = sessionmaker(bind=engine)
session = Session()

#
# stu1 = Student(name='zhoutao')
# stu2 = Student(name='jack')
# stu3 = Student(name='rose')
# study_obj1 = StudyRecord(day=1,status='YES',stu_id=1)
# study_obj2 = StudyRecord(day=1,status='YES',stu_id=1)
# study_obj3 = StudyRecord(day=1,status='YES',stu_id=2)
#
#
# session.add_all([stu1,stu2,stu3,study_obj1,study_obj2,study_obj3])

# session.add_all([study_obj1,study_obj2,study_obj3])


stu_obj1 = session.query(Student).filter(Student.name =='jack').first()
print(stu_obj1)

stu_obj2 = session.query(StudyRecord).filter(StudyRecord.stu_id == 1).first()
print(stu_obj2)
print(stu_obj2.student) # relatioship　在StudentRecord表中反差　student表中的数据，返回的是student的ｒｅｐｒ数据，注意只能在只有声明relationship表中查询


# session.commit()