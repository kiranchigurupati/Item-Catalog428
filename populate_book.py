from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db_setup import User, Genre, Base, BookItem

engine = create_engine('sqlite:///new_book_catalog.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

session = DBSession()
# the first user
User1 = User(name="Kiran Ch", email="chigurupatikiran97@gmail.com",
             picture='https://upload.wikimedia.org/wikipedia/commons/thumb/1/12/User_icon_2.svg/220px-User_icon_2.svg.png')
session.add(User1)
session.commit()

# Poetry Books
genre1 = Genre(user_id=1, name="Poetry", description = "Poetry is an art form in which human language is used for its aesthetic qualities in addition to, or instead of, its notional and semantic content.")

session.add(genre1)
session.commit()

book = BookItem(user_id=1, name="Where the Sidewalk Ends", description="Children\'s poetry collection written and illustrated by Shel Silverstein. Published by Harper and Row Publishers.",
                     type = "eBook", price="$2.50", author="Shel Silverstein", genre=genre1)

session.add(book)
session.commit()


book1 = BookItem(user_id=1, name="Leaves of Grass", description="The seminal work of one of the most influential writers of the nineteenth century.",
                     type="hardCopy",price="$3.50", author="Walt Whitman", genre=genre1)

session.add(book1)
session.commit()

book2 = BookItem(user_id=1, name="Howl and Other Poems", description="The single most influential poetic work of the post-World War II era, with over 900,000 copies now in print.",
                     type="hardCopy",price="$5.50", author="Allen Ginsberg", genre=genre1)

session.add(book2)
session.commit()

book3 = BookItem(user_id=1, name="Ariel", description="The beloved poet\'s brilliant, provoking, and always moving poems, including Ariel",
                     type = "eBook",price="$3.50", author="Sylvia Plath", genre=genre1)

session.add(book3)
session.commit()

book4 = BookItem(user_id=1, name="Paradise Lost", description="One of the greatest epic poems in the English language.",
                     type="hardCopy",price="$8.50", author="John Milton", genre=genre1)

session.add(book4)
session.commit()

book5 = BookItem(user_id=1, name="The Odyssey", description="Literature\'s grandest evocation of life's journey, and an individual test of moral endurance",
                     type = "eBook",price="$1.50", author="Homer", genre=genre1)

session.add(book5)
session.commit()

book6 = BookItem(user_id=1, name="The Iliad", description="One of the greatest war stories of all time",
                     type="hardCopy",price="$1.50", author="Homer", genre=genre1)

session.add(book6)
session.commit()


# Fantasy books
genre2 = Genre(user_id=1, name="Fantasy", description="Fantasy is a genre of fiction set in a fictional universe, often, but not always, without any locations, events, or people referencing the real world.")

session.add(genre2)
session.commit()
book7 = BookItem(user_id=1, name="The Chronicles of Narnia", description="Journeys to the end of the world, fantastic creatures, and epic battles between good and evil",
                     type="hardCopy",price="$3.50", author="C.S. Lewis ", genre=genre2)

session.add(book7)
session.commit()

book8 = BookItem(user_id=1, name="The Final Empire", description="In a world where ash falls from the sky, and mist dominates the night, an evil cloaks the land and stifles all life.",
                     type = "eBook",price="$5.50", author="Brandon Sanderson", genre=genre2)

session.add(book8)
session.commit()

book9 = BookItem(user_id=1, name="A Game of Thrones", description="Summers span decades. Winter can last a lifetime. And the struggle for the Iron Throne has begun.",
                     type="hardCopy",price="$3.50", author="George R.R. Martin", genre=genre2)

session.add(book9)
session.commit()

book10 = BookItem(user_id=1, name="Eragon", description="Eragon must navigate the dangerous terrain and dark enemies of an empire ruled by a king whose evil knows no bounds. ",
                     type = "eBook",price="$8.50", author=" Christopher Paolini ", genre=genre2)

session.add(book10)
session.commit()

print "DB is populated"
