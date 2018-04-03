#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Zhoutao
#create_date:2017-05-08-14:00
# Python 3.5

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import  Column,Integer,String,ForeignKey,UniqueConstraint,Index
from sqlalchemy.orm import sessionmaker,relationship
from sqlalchemy import create_engine

engine = create_engine('mysql+pymysql://root:newbie@127.0.0.1/test',max_overflow=5,echo=False)

Base = declarative_base()


class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer,primary_key=True,)
    name = Column(String(32))
    password = Column(String(32))

    __tableargs__ = (
        UniqueConstraint(name), #加上唯一自动有index
        Index('nameindex',name),
        Index('passwordindex',password),
    )

    def __repr__(self):
        return '<name--%s;password--%s>'%(self.name,self.password)

class Persons(Base):
    __tablename__ = 'persons'
    pid = Column(Integer,primary_key=True)
    nick_name = Column(String(32))
    fid = Column(Integer,ForeignKey('users.id')) # 外键关联users.id


Base.metadata.create_all(engine)

#增加
Session = sessionmaker(bind=engine)
session = Session()

obj_single = Users(name='tset11',password='password11')

obj_all = [
    Users(name='test1',password='password1'),
    Users(name='test2',password='password2'),
]


#
# session.add(obj_single)
# session.add_all(obj_all)
# session.commit()


#查
#查询
data1 = session.query(Users).filter_by(name='test1').all() #all所有数据取得一个列表
data2 = session.query(Users).filter_by(name='test1').first() #first取得第一个数据
data3 = session.query(Users).filter(Users.id>2).all() # 查询id > 2 的这里用filter 可以写大于
data4 = session.query(Users).filter(Users.id==2).all() # 查询id = 2 的这里用filter 等于要用 ==
data5 = session.query(Users).filter(Users.name=='test1').all() #
data6 = session.query(Users).filter(Users.name.in_(['test1','test2'])).all() # 表示查询出name是wr和ls的打印出来


#多条件查询
data7 = session.query(Users).filter(Users.id ==2).filter(Users.name=='test1').first() #多条件查询直接多个filter

print(data1)
print(data2)
print(data3)
print(data4)
print(data5)
print(data6)
print(data7)



#删除
# session.query(Users).filter(Users.id>1).delete()
# session.commit()

#修改

# session.query(Users).filter(Users.id == 1).update({'name':'n1'})
# session.commit()

dict_change_name = {'name':'n3'}
session.query(Users).filter(Users.id==1).update(dict_change_name,synchronize_session=False) #不对session进行同步，直接进行delete or update操作
# session.commit()