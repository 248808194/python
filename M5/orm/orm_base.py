#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Zhoutao
#create_date:2017-05-04-09:27
# Python 3.5

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import  declarative_base
from sqlalchemy import  Column,Integer,String
from sqlalchemy.orm import  sessionmaker

engine = create_engine('mysql+pymysql://root:newbie@127.0.0.1/test',encoding='utf8',echo=False)

Base = declarative_base() #生成orm基类
class User(Base):

    __tablename__ = 'user'
    id = Column(Integer,primary_key=True)
    name = Column(String(32))
    password = Column(String(64))

    def __repr__(self): #加一个repr方法打印出query获取的值
        return '<id:%s name:%s>'%(self.id,self.name)


Base.metadata.create_all(engine) #create_all 把所有继承Base的子类都创建执行了

#--------------------------------------------#


Session_class = sessionmaker(bind=engine)  # 创建与数据库的会话session class ,注意,这里返回给session的是个class,不是实例
Session = Session_class()  # 生成session实例 #相当于cursor

user_obj = User(name="alex", password="alex3714")  # 生成你要创建的数据对象
user_obj1 = User(name="zs", password="1alex3714")  # 生成你要创建的数据对象
user_obj2 = User(name="ls", password="2alex3714")  # 生成你要创建的数据对象
user_obj3 = User(name="wr", password="3alex3714")  # 生成你要创建的数据对象
# print(user_obj.name, user_obj.id)  # 此时还没创建对象呢，不信你打印一下id发现还是None
#
# Session.add(user_obj)  # 把要创建的数据对象添加到这个session里， 一会统一创建
# Session.add(user_obj1)  # 把要创建的数据对象添加到这个session里， 一会统一创建
# Session.add(user_obj2)  # 把要创建的数据对象添加到这个session里， 一会统一创建
# Session.add(user_obj3)  # 把要创建的数据对象添加到这个session里， 一会统一创建
# print(user_obj.name, user_obj.id,123)  # 此时也依然还没创建

# Session.commit()  # 现此才统一提交，创建数据


#查询
# date = Session.query(User).filter_by(name='alex').all() #all所有数据取得一个列表
# date = Session.query(User).filter_by(name='alex').first() #first取得第一个数据
# date = Session.query(User).filter(User.id>2).all() # 查询id > 2 的这里用filter 可以写大于
# date = Session.query(User).filter(User.id==2).all() # 查询id = 2 的这里用filter 等于要用 ==
# date = Session.query(User).filter(User.name=='alex').all() #
# data = Session.query(User).filter(User.name.in_(['wr','ls'])).all() # 表示查询出name是wr和ls的打印出来


#多条件查询
# data = Session.query(User).filter(User.id ==2).filter(User.name=='zs').first() #多条件查询直接多个filter


#修改,修改数据必须要查询出来在赋值修改才行，所以上面的查询是需要的
# data = Session.query(User).filter(User.id ==2).filter(User.name=='zs').first()
# data.name = 'newsz'
# data.password = 'newpasswd'
# Session.commit()
# print(data)

#回滚操作
# Session.add(User(name='pp',password='ppp'))
# print(Session.query(User).filter(User.name=='pp').all())
# Session.rollback()
# print(Session.query(User).filter(User.name=='pp').all())


#统计
# data = Session.query(User).filter(User.name.in_(['wr','ls'])).count() #统计出name 是 wr,ls的一共多少个，输出为2

#分组
from sqlalchemy import  func
data = Session.query(func.count(User.name),User.name).group_by(User.name).all()
# data = Session.query(func.count(User.name),User.name).group_by(User.name).first()
print(data,type(data))

#外键关联
