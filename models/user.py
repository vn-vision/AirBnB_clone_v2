#!/usr/bin/python3
"""This module defines a class User"""
<<<<<<< HEAD
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

=======
from models.base_model import BaseModel
>>>>>>> parent of 93b571e (Creating table USER)


class User(BaseModel):
    """This class defines a user by various attributes"""
<<<<<<< HEAD

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
=======
    email = ''
    password = ''
    first_name = ''
    last_name = ''
>>>>>>> parent of 93b571e (Creating table USER)
