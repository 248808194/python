#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Zhoutao
#create_date:2017-05-09-16:15
# Python 3.5

#一本书可以有多个作者，一个作者又可以出版多本书


from sqlalchemy import Table, Column, Integer,String,DATE, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql+pymysql://root:newbie@127.0.0.1/test?charset=utf8',max_overflow=5,echo=False)

Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()


# 另外一个创建表的方式，这张表单独交给orm管理，不需要通过类的方式去创建它,这张表是主动的关联 book 和author表
book_m2m_author = Table('book_m2m_author', Base.metadata,
                        Column('book_id',Integer,ForeignKey('books.id')),
                        Column('author_id',Integer,ForeignKey('authors.id')),
                        )



class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer,primary_key=True)
    name = Column(String(64))
    pub_date = Column(DATE)
    authors = relationship('Author',secondary=book_m2m_author,backref='books') #python 在内存上建立表和表的关系 # 建立和Author类的关系，通过Author可以去反差books表，secondary 指向给中间表。

    def __repr__(self):
        return self.name

class Author(Base):
    __tablename__ = 'authors'
    id = Column(Integer, primary_key=True)
    name = Column(String(32))

    def __repr__(self):
        return self.name

Base.metadata.create_all(engine)


#
# b1 = Book(name="跟Alex学Python")
# print(b1)
# a = session.query(Book).filter(Book.name=="跟Alex学Python").one()
# a3 = session.query(Author).filter(Author.name=='Rain').one()
# print(a,a3)
# a.authors.append(a3)
# b2 = Book(name="跟Alex学把妹")
# b3 = Book(name="跟Alex学装逼")
# b4 = Book(name="跟Alex学开车")
#
# a1 = Author(name="Alex")
# a2 = Author(name="Jack")
# a3 = Author(name="Rain")
#
#
# b1.authors = [a1,a2] # 将对应关系发送给中间表，以记录下书 和 作者的对应关系。
# b2.authors = [a1,a2,a3]
#
# session.add_all([b1,b2,b3,b4,a1,a2,a3

#通过书名查询作者
# obj = session.query(Book).filter_by(name='跟Alex学Python').first()
# print(obj)

obj1 = session.query(Author).filter_by(name='Alex').first()
print(obj1)
# print(obj1.name,obj1.books) # obj.books对应的是表名
# session.commit()