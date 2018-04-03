#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Zhoutao
#create_date:2017-05-15-16:51
# Python 3.5


from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import  Column,Integer,String,ForeignKey,UniqueConstraint,Index,Date,Enum,Table
from sqlalchemy.orm import sessionmaker,relationship
from sqlalchemy import create_engine
from sqlalchemy_utils import ChoiceType,PasswordType # 插件需要安装

engine = create_engine('mysql+pymysql://root:newbie@127.0.0.1/test',max_overflow=5,echo=False)

Base = declarative_base()

class Customer(Base):
    __tablename__ = 'customer'
    id = Column(Integer,primary_key=True)
    name = Column(String(64))
    billing_address_id = Column(Integer,ForeignKey('address.id'))
    shipping_address_id = Column(Integer,ForeignKey('address.id'))

    #遇到都要关联多个同样的表，时需要加上foreign_keys 指定具体哪一张表，否在插入数据的时候sqlalchemy会分不清到底插入哪个字段
    billing_address = relationship('Address',foreign_keys=[billing_address_id])
    shipping_address = relationship('Address',foreign_keys=[shipping_address_id])

    def __repr__(self):
        return  "<name:%s billing_address:%s shipping_address:%s>"%(self.name,self.billing_address,self.shipping_address)



class Address(Base):
    __tablename__ = 'address'
    id = Column(Integer,primary_key= True)
    street = Column(String(64))
    city = Column(String(64))
    state = Column(String(64))

    def __repr__(self):
        return "id:%s street:%s city:%s state:%s"%(self.id,self.street,self.city,self.state)



Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# add1 = Address(street='caowu.rd',city='XUHUI',state='SH')
# add2 = Address(street='nanjin.rd(E)',city='HUANGPU',state='SH')
# add3 = Address(street='gaoke.rd(W)',city='PUDONG',state='SH')
# #
# #
# session.add_all([add1,add2,add3])
# # session.commit()
# #
# c1 = Customer(name='zhoutao',billing_address=add1,shipping_address=add2) # 这里可以写ｉｄ，页可以直接写对象  # 如果需要加对象必须是用了relationship 的　foreign_keys
# c2 = Customer(name='jack',billing_address=add2,shipping_address=add3)
# session.add_all([c1,c2])
# session.commit()
obj1 = session.query(Customer).filter(Customer.name=='zhoutao').first()
print(obj1)



