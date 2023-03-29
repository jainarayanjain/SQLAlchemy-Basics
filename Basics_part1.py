from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
engine = create_engine('sqlite:///college.db', echo = None)
# The function has two arguments, one is the name of database and
# other is an echo parameter when set to True will generate the activity log

meta = MetaData()
conn=engine.connect()
students = Table(
   'students', meta,
   Column('id', Integer, primary_key = True),
   Column('name', String),
   Column('lastname', String),
)



# insertion of data into table

n='Aman'
l='ji'
i=6

# ins=students.insert().values(id=3,name='Raghav',lastname='Gupta')
# result=conn.execute(ins)


# ins=students.insert().values(:id,:name,:lastname)
# result=conn.execute(ins,(i,n,l))


#Multiple Insert

# conn.execute(students.insert(), [
#    {'name':'Ravi', 'lastname':'Kapoor'},
#    {'name':'Rajiv', 'lastname' : 'Khanna'},
#    {'name':'Komal','lastname' : 'Bhandari'},
#    {'name':'Abdul','lastname' : 'Sattar'},
#    {'name':'Priya','lastname' : 'Rajhans'},
# ])


# Normal Select Query

# s=students.select()
# result=conn.execute(s)
# print(result.fetchone())

# Select using Where

# s = students.select().where(students.c.id == 2)    #c is the alias for column
# print(conn.execute(s).fetchall())

# Update

# stmt = students.update().where(students.c.lastname == 'Gupta').values(lastname = 'Kapoor')
# conn.execute(stmt)

#Delete

# stmt = students.delete().where(students.c.lastname == 'Kapoor')
# conn.execute(stmt)

