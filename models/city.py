#!/usr/bin/python3
"""This is the city class"""
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
<<<<<<< HEAD
from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from models.place import Place
=======
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
>>>>>>> refs/remotes/origin/master


class City(BaseModel, Base):
    """This is the class for City
    Attributes:
        state_id: The state id
        name: input name
    """
    __tablename__ = "cities"
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
<<<<<<< HEAD
    places = relationship("Place", cascade='all, delete, delete-orphan',
                          backref="cities")
=======

    # Create link to places
    places = relationship('Place', back_populates='cities',
                          cascade='all, delete-orphan')
>>>>>>> refs/remotes/origin/master
