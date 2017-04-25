from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Restaurant, MenuItem, Base

engine = create_engine('sqlite:///restaurantmenu.db?check_same_thread=False')
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
    restaurants = session.query(Restaurant.name).order_by(Restaurant.name.asc()).all()
    # temp = session.query(Restaurant.name).order_by(Restaurant.name.asc()).all()
    # restaurants = [t[0] for t in temp]
    # for r in restaurants:
    # 	print r
    return restaurants

def addNewRestaurant(val):
	new_res = Restaurant(name = val)
	session.add(new_res)
	session.commit()

def validateRestaurant(val):
	res = session.query(Restaurant).filter_by(name = val).one()
	if res.name:
		return True
	else:
		return False 
#getAllRestaurants()