import psycopg2
from json import load
from sqlalchemy import Table, Column, Integer, String, ForeignKey, DateTime, create_engine
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
# from flask_wtf import Form
# from wtforms import TextField, DateTimeField
# from forms import EventForm

Base = declarative_base()
#g
# definitions of SQLAlchemy database classes
class Event(Base):
    __tablename__ = 'event'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    category = Column(String)
    start = Column(DateTime)
    end = Column(DateTime)
    location = Column(String)

    def __init__(self, id, name, category, start, end, location):
        self.id = id
        self.name = name
        self.category = category
        self.start = start
        self.end = end
        self.location = location

    def __repr__(self):
        return "<Event({}, {}-{})>".format(self.name, self.start, self.end)

class Location(Base):
    __tablename__ = 'location'
    id = Column(Integer, primary_key=True)
    city = Column(String)
    country = Column(String)

    def __init__(self, id, city, country):
        self.id = id
        self.city = city
        self.country = country

    def __repr__(self):
        return "<Location({}, {})>".format(self.city, self.country)

class Category(Base):
    __tablename__ = 'category'
    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __repr__(self):
        return "<Category({})>".format(self.name)

print("TABLES CREATED")




# create the engine
engine = create_engine('postgres://fzoxyvegfbbwwp:dcc7d0363278a31d092ec89d957cac2874f27c0caad1261ffb01092c3c933bb2@ec2-54-235-90-107.compute-1.amazonaws.com:5432/d1veuupffk4555', echo = True)
Session = sessionmaker(bind=engine)

db = Session()

print("SESSION CREATED")

def db_create():

    # Base.metadata.drop_all(engine)
    # print("DROP ALL")
    # Base.metadata.create_all(engine)
    # print("CREATE ALL")
    # db.commit()

    # # connection for knuth cities table
    # conn = psycopg2.connect(user='hawkol01', dbname='world', host='knuth.luther.edu')
    # data = conn.cursor()
    #
    # # populate the location table
    # data.execute("""SELECT * FROM city;""")
    # res = data.fetchall()
    #
    # for i in res:
    #     new_place = Location(id=i[0], city=i[1], country=i[2])
    #     db.add(new_place)
    #
    # db.commit()

    print("LOCATION POPULATED")

# db_create()

#connection to Heroku database for insertion
conn2 = psycopg2.connect('postgres://fzoxyvegfbbwwp:dcc7d0363278a31d092ec89d957cac2874f27c0caad1261ffb01092c3c933bb2@ec2-54-235-90-107.compute-1.amazonaws.com:5432/d1veuupffk4555')
data2 = conn2.cursor()
print("CONNECTED TO HEROKU")

def clearTable():
    data2.execute("""DELETE FROM event;""")
    data2.execute("""DELETE FROM category WHERE id>0;""")
    db.commit()
#clearTable()
print("PREVIOUS TABLE CLEARED")
# populate the event table
# data2.execute("""SELECT count(*) FROM event;""")
# num = data2.fetchall()

# function called from app.py to create a new event
def crevnt(name, category, start, end, location):
    data2.execute("""SELECT count(*) FROM event;""")
    num = data2.fetchall()
    eid = num[0][0]
    new_event = Event(eid, name, category, start, end, location)
    db.add(new_event)
    db.commit()
print("EVENTS COUNTED")

# grab events from database for index()
# data2.execute("""SELECT * FROM event;""")
# events = data2.fetchall()
def show_events():
    data2.execute("""SELECT * FROM event;""")
    events = data2.fetchall()
    print("RETURNING EVENTS")
    return events

# populate the category table
# data2.execute("""SELECT count(*) FROM category;""")
# catnum = data2.fetchall()

# function called from app.py to create a new category
def crt_ctgry(name):
    data2.execute("""SELECT count(*) FROM category;""")
    catnum = data2.fetchall()
    catid = catnum[0][0]
    print("CAAAATID =")
    print(catid)
    print(name)
    print(type(name))
    new_category = Category(catid, name)
    db.add(new_category)
    db.commit()
    #Session.rollback()
print("CATEGORIES COUNTED")

db.commit()

print("ALL COMMITTED")

# returns the list of categories
def getCat():
    data2.execute("""SELECT DISTINCT name FROM category;""")
    stuff=data2.fetchall()
    l = []
    for i in stuff:
        t = (i[0],i[0])
        l.append(t)
    print(l)

    return l

# returns the list of cities and country codes
def getLoc():
    l = []
    c = 0
    data2.execute("""SELECT name, country FROM location""")
    stuff=data2.fetchall()
    for i in stuff:
        astr = i[0] + "," + i[1]
        t = (count,astr)
        count += 1
        l.append(t)
    return l
