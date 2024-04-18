#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """ The city class, contains state ID and name """

    # create table cities
    __tablename__ = 'cities'

    # create attribute name, type string and can't be null
    name = Column(String(128), nullable=False)

    # create foreign key linking city to state
    state_id = Column(String(60), ForeignKey('states.id', ondelete='CASCADE'),
                      nullable=False)

    # Create link to places
    places = relationship('Place', back_populates='cities',
                          cascade='all, delete-orphan')
