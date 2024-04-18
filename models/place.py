#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship


class Place(BaseModel, Base):

    # create table place
    __tablename__ = 'places'

    # create the different attributes for the Place
    """ A place to stay """
    # create foreign keys in table places referencing other models
    city_id = Column(String(60), ForeignKey('cities.id', ondelete='CASCADE'),
                     nullable=False)
    user_id = Column(String(60), ForeignKey('users.id', ondelete='CASCADE'),
                     nullable=False)

    # continue with other attributesYes
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []

    # define relationship between place and: user
    user = relationship('User', back_populates='places')

    # :City
    cities = relationship('City', back_populates='places')
