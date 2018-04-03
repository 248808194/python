#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Zhoutao
#create_date:2017-05-09-13:53
# Python 3.5

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


class Customer(Base):
    __tablename__ = 'customer'
    id = Column(Integer, primary_key=True)
    name = Column(String(64))

    billing_address_id = Column(Integer, ForeignKey("address.id"))
    shipping_address_id = Column(Integer, ForeignKey("address.id"))

    billing_address = relationship("Address",foreign_keys=[billing_address_id])
    shipping_address = relationship("Address",foreign_keys=[shipping_address_id])

    def __repr__(self):
        return 'name:%s,billing_address_id:%s,shipping_address_id:%s'%(self.name,self.billing_address_id,self.shipping_address_id)


class Address(Base):
    __tablename__ = 'address'
    id = Column(Integer, primary_key=True)
    street = Column(String(64))
    city = Column(String(64))
    state = Column(String(64))


Base.metadata.create_all(engine)


Session = sessionmaker(bind=engine)
session = Session()

addr1 =Address(street='xujiahui',city='xuhui',state='shanghai')
addr2 =Address(street='EXPO',city='pudong',state='shanghai')
addr3 =Address(street='xintiandi',city='huangpu',state='shanghai')

# session.add_all([addr1,addr2,addr3])


c1 = Customer(name='rose',billing_address=addr1,shipping_address=addr1)
c2 = Customer(name='jack',billing_address=addr2,shipping_address=addr2)
c3 = Customer(name='bill',billing_address=addr1,shipping_address=addr3)

# session.add_all([c1,c2,c3])
obj = session.query(Customer).filter(Customer.name=='jack').first() # 查询
print(obj)
session.commit()
