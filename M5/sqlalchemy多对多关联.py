#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Zhoutao
#create_date:2017-05-16-14:18
# Python 3.5

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import  Column,Integer,String,ForeignKey,UniqueConstraint,Index,Date,Enum,Table
from sqlalchemy.orm import sessionmaker,relationship
from sqlalchemy import create_engine
from sqlalchemy_utils import ChoiceType,PasswordType # 插件需要安装
from  sqlalchemy import func
from sqlalchemy import and_, or_,any_
engine = create_engine('mysql+pymysql://root:newbie@127.0.0.1/test',max_overflow=5,echo=False)

Base = declarative_base()


techer_m2m_lesson = Table('techer_m2m_lesson',Base.metadata,
                          Column('techer_id',Integer,ForeignKey('techer.id')),
                          Column('lesson_id',Integer,ForeignKey('lesson.id')),
                          )

class Techer(Base):

    __tablename__ = 'techer'
    id = Column(Integer,primary_key=True)
    techer_name = Column(String(64),nullable=False)
    lessons = relationship('Lesson',secondary=techer_m2m_lesson,backref='techers')

    def __repr__(self):
        return self.techer_name

class Lesson(Base):
    __tablename__ = 'lesson'
    id = Column(Integer,primary_key=True)
    lesson_name = Column(String(64),unique=True)


    def __repr__(self):
        return self.lesson_name




Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

#添加老师

#
t1 = Techer(techer_name='MR.wang')
t2 = Techer(techer_name='MR.zhou')
t3 = Techer(techer_name='MR.huang')
L1 = Lesson(lesson_name='Python')
L2 = Lesson(lesson_name='Linux')
L3 = Lesson(lesson_name='Go')
L4 = Lesson(lesson_name='To')

a = session.query(Techer).filter(Techer.techer_name=='MR.huang').first()
tmp_list = []
b = session.query(Lesson).filter(Lesson.id.in_([13,3])).all()
print(b,type(b),type(b[0]))

# [a.lessons.remove(x) for x in b]


# session.commit()
# print(session.query(Techer).filter(Techer.techer_name=='MR.huang').first().lessons)
# a = session.query(Techer).filter(Techer.techer_name=='MR.huang').first()
# b = session.query(Lesson).filter(Lesson.id==3).first()
# a.lessons.remove(b)
# session.commit()



#
# obj = [i.id for i in session.query(Techer).filter(Techer.techer_name == 'MR.zhou2').first().lessons]
# print(obj)

# obj = session.query(Techer).filter(Techer.techer_name == 'MR.zhou2').first()
#
# if len(obj.lessons) > 1:
#     for i in obj.lessons:
#         print(i.lesson_name,type(i.lesson_name))
#         print(i.lesson_name == 'Go')
#         if i.lesson_name == 'Go':
#             obj.lessons.remove(session.query(Lesson).filter(Lesson.lesson_name == i.lesson_name).first())
#
#         else:
#             print('go not found')
#     obj.lessons.append(session.query(Lesson).filter(Lesson.lesson_name == 'python').first())


#
# session.commit()
#
# print(obj.lessons)


#MR zhou2 id 2
# TO LESSON ID  2 3 change to 1 3 1:python


# session.commit()


# aa = session.query(Techer).filter(Techer.techer_name=='MR.zhou').first()
# print(aa.lessons)
#
# session.commit()


# # #
#
# # session.commit()
# #
# t1.lessons = [L1,L2,L3] #建立老师和课程的对应关系
# t2.lessons = [L2,L3]
# t3.lessons = [L3]
# # # #
# # # # #提交数据
# session.add_all([
#     t1,t2,t3,L1,L2,L3
# ])
# # #
# # #
# session.commit()

