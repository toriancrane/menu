from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Restaurant, MenuItem, Base

engine = create_engine('sqlite:///restaurantmenu.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine
 
DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

def getAllRestaurants():    
    """ Query all of the restaurants and return the results in ascending alphabetical order """
    temp = session.query(Restaurant.name).order_by(Restaurant.name.asc()).all()
    # temp = []
    # for r in restaurants:
    # 	temp.append(r.encode('ascii', 'utf-8'))
    # return temp
    restaurants = [t[0] for t in temp]
    # for r in restaurants:
    # 	print r
    return restaurants

#getAllRestaurants()