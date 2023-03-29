# this contains orm concetps using base class

# we cannot use core method in this type of setup

"""This type will not work when we will use Base Class """
# s=customers.select()
# result=conn.execute(s)
# print(result.fetchone())


from sqlalchemy import Column, Integer, String,insert
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///sales.db', echo=None)
conn=engine.connect()
Base = declarative_base()
Session=sessionmaker(bind=engine)
session=Session()




class Customers(Base):
    __tablename__ = 'customers'
    id = Column(Integer, primary_key=True)

    name = Column(String)
    address = Column(String)
    email = Column(String)


#Base.metadata.create_all(engine)


"""Insertion of Data into Table"""

# c1 = Customers(name = 'Ravi Kumar', address = 'Station Road Nanded', email = 'ravi@gmail.com')
# session.add(c1)
# session.commit()
a="Ravi"
b="ds"
c="sdfsdf"

c1 = Customers(name =a, address =b, email = c)
session.add(c1)
session.commit()

"""For Selecting Data"""

# result = session.query(Customers).all()
# for r in result:
#     print(r.name)

