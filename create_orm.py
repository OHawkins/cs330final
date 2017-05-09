import psycopg2
from json import load
from sqlalchemy import Table, Column, Integer, String, ForeignKey, DateTime, create_engine
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Event(Base):
    __tablename__ = 'event'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    category = Column(String)
    start = Column(DateTime)
    end = Column(DateTime)
    location = Column(String)

    def __repr__(self):
        return "<Event({}, {}-{})>".format(self.name, self.start, self.end)


class Location(Base):
    __tablename__ = 'location'
    id = Column(Integer, primary_key=True)
    city = Column(String)
    country = Column(String)

    def __repr__(self):
        return "<Location({}, {})>".format(self.city, self.country)


class Category(Base):
    __tablename__ = 'category'
    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __repr__(self):
        return "<Category({})>".format(self.name)



engine = create_engine('postgresql://hawkol01@knuth.luther.edu/hawkol01', echo=True)
session = sessionmaker(bind=engine)

db = session()

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

conn = psycopg2.connect(user='hawkol01', dbname='world', host='knuth.luther.edu')
data = conn.cursor()

data.execute("""SELECT * FROM city;""")

res = data.fetchall()


for i in res:
    new_place = Location(id=i[0], city=i[1], country=i[2])
    db.add(new_place)
for i in range(10):
    print(new_place)
db.commit()

# conn = psycopg2.connect(user='hawkol01', host='knuth.luther.edu', port=2345)
# cur = conn.cursor()
#
# cur.execute("""CREATE TABLE event (
#             PRIMARY KEY id serial unique,
#             name varchar(50),
#             location varchar(100),
#             start timestamp,
#             end timestamp,
#             category varchar(50) REFERENCES category(id)
#             );""")
#
# cur.execute("""CREATE TABLE place (
#             PRIMARY KEY id serial unique,
#             street varchar(20),
#             city varchar(20),
#             state varchar(20),
#             country varchar(20),
#             zip integer
#             );""")
#
# cur.execute("""CREATE TABLE category (
#             PRIMARY KEY id serial unique,
#             name varchar(20) unique
#             );""")
#
# conn.commit()
