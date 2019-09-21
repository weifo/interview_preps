'''
第 0001 题： 做为 Apple Store App 独立开发者，你要搞限时促销，为你的应用生成激活码（或者优惠券），使用 Python 如何生成 200 个激活码（或者优惠券）？

第 0002 题: 将 0001 题生成的 200 个激活码（或者优惠券）保存到 MySQL 关系型数据库中。
'''
from sqlalchemy import create_engine,Column,Integer,String,DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from uuid import uuid4

engine = create_engine('mysql+pymysql://root:password@127.0.0.1:3306/rest_demo', echo=False)
Base = declarative_base()

class Coupon(Base):
    __tablename__='coupon'

    id=Column(Integer,primary_key=True)
    value=Column(String(50))

    def __repr__(self):
        return "{} is {}".format(self.id,self.value)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session=Session()

for i in range(100):
    value=str(uuid4())
    uid=Coupon(value=value)
    session.add(uid)
session.commit()