from sqlalchemy import *
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

engine = create_engine('sqlite:///login2.db', echo=True)
Base = declarative_base()

########################################################################
class Ticket(Base):
    """"""
    __tablename__ = "tickets"

    ticket_id = Column(Integer,primary_key=True)
    username = Column(String)
    city_id = Column(Integer)
    city_name = Column(String)
    theatre_id = Column(Integer)
    theatre_name = Column(String)
    movie_id = Column(Integer)
    movie_name = Column(String)
    show_id = Column(Integer)
    show_time = Column(String)
    seats = Column(String)




    #----------------------------------------------------------------------
    def __init__(self, ticket_id, username, city_id, city_name, theatre_id, theatre_name, movie_id, movie_name, show_id, show_time, seats):

        self.ticket_id = ticket_id
        self.username = username
        self.city_id = city_id
        self.city_name = city_name
        self.theatre_id = theatre_id
        self.theatre_name = theatre_name
        self.movie_id = movie_id
        self.movie_name = movie_name
        self.show_id = show_id
        self.show_time = show_time
        self.seats = seats


# create tables
Base.metadata.create_all(engine)
