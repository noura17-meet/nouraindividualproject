from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

from database import *

engine = create_engine('sqlite:///crudlab.db')
Base.metadata.create_all(engine)
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

# Books = [
# {'name' : 'The Hobbit', 'genre' : 'Fantasy', 'photo' : 'https://images-na.ssl-images-amazon.com/images/M/MV5BODAzMDgxMDc1MF5BMl5BanBnXkFtZTgwMTI0OTAzMjE@._V1_UX182_CR0,0,182,268_AL_.jpg',
# 'author' : ' J.R.R tolkien' , 'publish_year': '1937', 'rate': '5' , 'plot' :"Bilbo Baggins is a Hobbit in this place called Middle-Earth. He is a tiny little fuzzy dude who lives in a tunnel. One day this wizard named Gandalf and these 13 dwarves visit him. The dwarves wanna Go to Lonely Mountain and get their treasure back from the evil dragon Smaug."},
# {'name' : 'Don Quixote' , 'ganre' : 'History', 'photo' : 'https://images-na.ssl-images-amazon.com/images/P/079450955X.jpg', 'author': 'Miguel de Cervantes', 
# 'publish_year' : '1937' , 'rate' : '3.8' , 'plot' : 'The hero in this book is a crazy dude who loses all of his fantasy -battles-. Alonso Quixano (Don Quixote): Alonso is a sweet older man who is absolutely nuts. He reads books about knights and starts believing he is a knight called Don Quixote de La Mancha'},
# {'name':'Harry Potter and the prisoner of azkaban', 'Genre':'Fantasy litterature', 'photo':'http://vignette3.wikia.nocookie.net/harrypotter/images/1/11/Prisoner_of_Azkaban_cover.jpg/revision/latest?cb=20070328184627', 'Author' : 'J. K Rowling', 'publish_year' : '1999', 'rate' : '5' , 'plot' :"Harry is back at the Dursleys, where he sees on Muggle television that a prisoner named Sirius Black has escaped. Harry involuntarily inflates Aunt Marge when she comes to visit after she insults Harry and his parents. This leads to his running away and getting picked up by the Knight Bus. He travels to Diagon Alley, where he meets Cornelius Fudge, the Minister for Magic, who asks Harry to stay in Diagon Alley for the remaining three weeks before the start of the school year at Hogwarts."},
# ]


# for Book in Books:
#     newBook = Book(name=Book['name'], genre =Book['genre'], photo=Book['photo'], author=Book['author'])
#     session.add(newBook)
#     session.commit()
 





noura=User(
    name = 'noura barakat',
    email = 'nourabarakat05@gmail.com',
    password = '111'
    )

session.add(noura)
session.commit()




