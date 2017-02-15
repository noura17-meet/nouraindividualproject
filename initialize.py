from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

from database import *

engine = create_engine('sqlite:///crudlab.db')
Base.metadata.create_all(engine)
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

hobbit = Book(
	title = "The Hobbit",
	genre = "Fantasy",
	Author = "J. R. R. Tolkien", 
	publish_year= 1937,
	rate = 5 ,
	plot ="Bilbo Baggins is a Hobbit in this place called Middle-Earth. He is a tiny little fuzzy dude who lives in a tunnel. One day this wizard named Gandalf and these 13 dwarves visit him. The dwarves wanna Go to Lonely Mountain and get their treasure back from the evil dragon Smaug." )


noura = User(
    name = 'noura barakat',
    email = 'nourabarakat05@gmail.com',
    password = '111'
    )

session.add(noura)
session.commit()