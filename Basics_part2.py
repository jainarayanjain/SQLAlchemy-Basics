from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, \
    ForeignKey, select, and_, union

engine = create_engine('sqlite:///school.db', echo=None)
meta = MetaData()
conn = engine.connect()
students = Table(
    'students', meta,
    Column('id', Integer, primary_key=True),
    Column('name', String),
    Column('lastname', String),
)

addresses = Table(
    'addresses', meta,
    Column('id', Integer, primary_key=True),
    Column('st_id', Integer, ForeignKey('students.id')),
    Column('postal_add', String),
    Column('email_add', String))

# meta.create_all(engine)

# Fetching records from two tables

# s = select([students, addresses]).where(students.c.id == addresses.c.st_id)
# rows=conn.execute(s)
# for r in rows:
#    print(r)

# Join

# j = students.join(addresses, students.c.id == addresses.c.st_id)
# stmt = select([students]).select_from(j)
# result = conn.execute(stmt)
# print(result.fetchall())

# Conjuction Operators

# stmt = select([students]).where(and_(students.c.name == 'Ravi', students.c.id < 3))
# result = conn.execute(stmt)
# print(result.fetchall())


# stmt = select([students]).where(or_(students.c.name == 'Ravi', students.c.id <3))

u = union(addresses.select().where(addresses.c.email_add.like(
    '%@gmail.com')),
    addresses.select().where(addresses.c.email_add.like('%@yahoo.com')))
result = conn.execute(u)

print(result.fetchall())
