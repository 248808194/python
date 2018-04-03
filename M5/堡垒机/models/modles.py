#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Zhoutao
#create_date:2017-05-15-09:47
# Python 3.5
import sys

import sys,os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import  Column,Integer,String,ForeignKey,UniqueConstraint,Index,Date,Enum,Table
from sqlalchemy.orm import sessionmaker,relationship
from sqlalchemy import create_engine
from sqlalchemy_utils import ChoiceType # 插件需要安装sqlamchemy_utils
from conf.settings import ConnParams

engine = create_engine(ConnParams,max_overflow=5,echo=False)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()
#


user_m2m_bindhost = Table('user_m2m_bindhost',Base.metadata,
                           Column('userprofile_id',Integer,ForeignKey('userprofile.id')),
                           Column('bindhost_id',Integer,ForeignKey('bind_host.id'))
                          )


group_m2m_bindhost = Table('group_m2m_bindhost',Base.metadata,
                           Column('group_id',Integer,ForeignKey('host_group.id')),
                           Column('bindhost_id',Integer,ForeignKey('bind_host.id'))
                          )

userprofile_m2m_group = Table('userprofile_m2m_group',Base.metadata,
                           Column('group_id',Integer,ForeignKey('host_group.id')),
                           Column('userprofile_id',Integer,ForeignKey('userprofile.id'))
                          )


class Host(Base): #主机表
    __tablename__ = 'host'

    id = Column(Integer,primary_key=True)
    hostname = Column(String(64),unique=True)
    ip = Column(String(64),unique=True)
    port = Column(Integer,default=22)



    def __repr__(self):
        return self.hostname


#
# session.add_all([H1,H2,H3])




class RemoteUser(Base): #远程主机用户表
    __tablename__ = 'remoteuser'

    __table_args__ = (UniqueConstraint('auth_type','username','password',name= '_user_passwd_uc'),)
    id = Column(Integer,primary_key=True)
    username = Column(String(64))
    password = Column(String(128),)
    # auth_type = Column(Enum(0,1),default=0) # 0 = password ,1 = key , 可通过插件sqlalchemy_utils来实现
    AuthTypes = [
        ('ssh-passwd','SSH/Password'),#第一个存放在数据库下的值,通过sqlalchemy取出来的是第二个值
        ('ssh-key','SSH/KEY'),
    ]

    auth_type = Column(ChoiceType(AuthTypes))


    def __repr__(self):
        return self.username
#

#
# session.add_all([R1,R2,R3])



class UserProfile(Base): #堡垒机机器上的系统用户表
    __tablename__ = 'userprofile'

    id = Column(Integer,primary_key=True)
    username = Column(String(64),unique=True)
    password = Column(String(128))
    #
    bindhosts = relationship('BindHost',secondary='user_m2m_bindhost',backref='userprofiles')
    groups = relationship('Group',secondary='userprofile_m2m_group',backref='userprofiles')

    #一台机器属于多个用户,一个用户可以访问多个机器 ,多对多


    def __repr__(self):
        return self.username





class Group(Base):
    __tablename__ = 'host_group'
    id = Column(Integer,primary_key=True)
    name = Column(String(64))
    print('exclution group class ')
    bindhosts = relationship('BindHost',secondary='group_m2m_bindhost',backref='groups')

    def __repr__(self):
        return self.name





class BindHost(Base):
    __tablename__ = 'bind_host'
    __table_args__ = (UniqueConstraint('remoteuser_id','host_id',name= '_remoteuser_host_uc'),)
    id = Column(Integer,primary_key=True)
    remoteuser_id = Column(Integer,ForeignKey('remoteuser.id'))
    host_id = Column(Integer,ForeignKey('host.id'))
    print('exclution bindhosts class ')
    remoteuser = relationship('RemoteUser',backref = 'bindhosts')
    host = relationship('Host',backref = 'bindhosts')






    def __repr__(self):

        return '<%s - %s>'%(self.host.id,self.remoteuser.username)

Base.metadata.create_all(engine)



H1 = Host(hostname='server1',ip='1.1.1.1',port=22)
H2 = Host(hostname='server2',ip='1.1.1.2',port=22)
H3 = Host(hostname='server3',ip='1.1.1.3',port=22)

R1 = RemoteUser(username='Ruser1',password='123456',auth_type='ssh-passwd')
R2 = RemoteUser(username='Ruser2',password='223456',auth_type='ssh-passwd')
R3 = RemoteUser(username='Ruser3',password='323456',auth_type='ssh-passwd')
#
B1=BindHost(remoteuser_id=1,host_id=1)
B2=BindHost(remoteuser_id=2,host_id=2)
B3=BindHost(remoteuser_id=3,host_id=3)

G1=Group(name='sh',bindhosts=[B1,B2])
G2=Group(name='bj',bindhosts=[B2,B3])

U1 = UserProfile(username='zhoutao',password='zhoutao',bindhosts=[B1,B2],groups=[G1])
U2 = UserProfile(username='jack',password='jack',bindhosts=[B3,B2],groups=[G2])
U3 = UserProfile(username='rain',password='rain',bindhosts=[B1,B3])

# session.add_all([
#     H1,H2,H3,R1,R2,R3,B1,B2,B3,G1,G2,U1,U2,U3
# ])

# session.commit()

aa = session.query(UserProfile).filter(UserProfile.username=='zhoutao',UserProfile.password=='zhoutao').first()

single_host_obj = aa.groups[0].bindhosts[0] #通过aa.groups去查其实就是ｓｑｌａｌｃｈｅｍｙ内部将Group类转换成一个对象,去执行这个对象，
print(single_host_obj,type(single_host_obj))
username = single_host_obj.remoteuser.username
password = single_host_obj.remoteuser.password
print(username)
print(password)


# session.commit();



#

# session.commit()
# if __name__ == '__main__':
#     Base.metadata.create_all(engine)
