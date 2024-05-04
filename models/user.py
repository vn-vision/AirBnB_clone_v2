#!/usr/bin/python3
<<<<<<< HEAD
"""This is the user class"""
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from models.place import Place
from models.review import Review


class User(BaseModel, Base):
    """This is the class for user
    Attributes:
        email: email address
        password: password for you login
        first_name: first name
        last_name: last name
    """
    __tablename__ = "users"
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))
    places = relationship("Place", cascade='all, delete, delete-orphan',
                          backref="user")
    reviews = relationship("Review", cascade='all, delete, delete-orphan',
                           backref="user")
     
=======
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """This class defines a user by various attributes"""

    # create table user
    __tablename__ = 'users'

    # Add the different attributes of the user, columns
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)

    # show relationship between users and places
    '''
    back_populates parameter in the relationship allows bidirectional
    navigation (Place objects can access their associated User
    via user attribute)
    '''
    places = relationship('Place', back_populates='user',
                          cascade='all, delete-orphan')
<<<<<<< HEAD
>>>>>>> refs/remotes/origin/master
=======

    reviews = relationship("Review", backref="user", cascade="delete")
>>>>>>> refs/remotes/origin/master
