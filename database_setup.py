import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class Restaurant(Base):
	""" Corresponds to the restaurant table """
	# Table information
	__tablename__ = 'restaurant'

	# Mappers
	r_name = Column(String(80), nullable = False)
	r_id = Column(Integer, primary_key = True) 


class MenuItem(Base):
	""" Corresponds to the MenuItem table """
	# Table information
	__tablename__ = 'menu_item'

	# Mappers
	m_name = Column(String(80), nullable = False)
	m_id = Column(Integer, primary_key = True)
	m_course = Column(String(250))
	m_description = Column(String(250))
	m_price = Column(String(8))
	r_id = Column(Integer, ForeignKey('restaurant.r_id'))
	restaurant = relationship(Restaurant)

engine = create_engine(
	'sqlite:///restaurantmenu.db')

Base.metadata.create_all(engine)