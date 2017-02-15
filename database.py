from sqlalchemy import Column, Date, Float, ForeignKey, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.dialects import postgresql

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(60))
    email = Column(String(60))
    password = Column(String(60))

class Book(Base):
    __tablename__= 'books'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    genre = Column(String)
    Author = Column(String)
    publish_year= Column(String)
    plot = Column(String)
    rate = Column(Float)

engine = create_engine('sqlite:///forum.db')
Base.metadata.create_all(engine)
DBsession = sessionmaker(bind=engine, autoflush = False)
session = DBsession()
