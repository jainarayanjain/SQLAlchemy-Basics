from sqlalchemy import Column, Integer, String, ForeignKey, Table,create_engine,insert
from sqlalchemy.orm import relationship, backref,sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("sqlite:///db.sqlite3", echo=None)

Base = declarative_base()
Session=sessionmaker(bind=engine)
session=Session()

class Author(Base):
    __tablename__ = "author"
    author_id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)

class Book(Base):
    __tablename__ = "book"
    book_id = Column(Integer, primary_key=True)

#Base.metadata.create_all(engine)
# stmt = Author(author_id=1, first_name="Spongebob Squarepants",last_name="Spongebob Squarepants")
# session.add(stmt)
# session.commit()

# students=session.query(Author)
#
# for s in students:
#     print(s.first_name)

# students=session.query(Author).order_by(Author.author_id)
# for s in students:
#     print(s.first_name)


#updation of record
student=session.query(Author).filter(Author.author_id==1).first()
# student.first_name='jai'
# session.commit()

session.delete(student)
session.commit()