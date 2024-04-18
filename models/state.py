#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String


class State(BaseModel, Base):
    """ State class """

    __tablename__ = 'states'

    name = Column(String(128), nullable=False)

    # Define relationship with city
    cities = relationship(
                'City', backref='state', cascade='all, delete-orphan')

<<<<<<< HEAD
    '''# Define getter attribute cities
=======
    '''
    # Define getter attribute cities
>>>>>>> refs/remotes/origin/master
    @property
    def cities(self):
        """ Getter attribute that returns list of city instance
        with matching state_id"""
        from models import storage
        from models.city import City
        return [city for city in storage.all(City)
<<<<<<< HEAD
                if city.state_id == self.id]'''
=======
                if city.state_id == self.id]
    '''
>>>>>>> refs/remotes/origin/master
