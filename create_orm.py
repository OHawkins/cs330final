import psycopg2
from json import load
from sqlalchemy import Table, Column, Integer, String, ForeignKey, DateTime create_engine
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Event(Base):
    __tablename__ = 'event'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    start = Column(DateTime)
    end = Column(DateTime)
    category = Column(String)

    location = relationship("Location",
                            secondary=event_city,
                            back_populates="containing")



    def __repr__(self):
        return "<Event({}, {}-{})>".format(self.name, self.start, self.end)

class Location(Base):
    __tablename__ = 'location'

    id = Column(Integer, primary_key=True)

    city = Column(String)
    state = Column(String)
    country = Column(String)
    zip = Column(Integer)

    containing = relationship()

    def __repr__(self):
        return "<Location({} {}, {} {}, {})>".format(self.street, self.city, self.state, self.zip, self.country)

class Category(Base):
    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __repr__(self):
        return "<Category({})>".format(self.name)



engine = create_engine('postgresql://hawkol01@localhost/finalcalorm')
session = sessionmaker(bind=engine)

db = Session()

Base.metatdata.drop_all(engine)
Base.metatdata.create_all(engine)


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
