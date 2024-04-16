#!/usr/bin/python3
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base


class DBuStorage:
    """
    this class manages databse storage with SQLAlchemy
    """

    __engine = None
    __session = None

    def __init__(self):
        """ initializes DBStorage instance """
        user = os.getenv("HBNB_MYSQL_USER")
        pwd = os.getenv("HBNB_MYSQL_PWD")
        host = os.getenv("HBNB_MYSQL_HOST", "localhost")
        db = os.getenv("HBNB_MYSQL_DB")
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            user, pwd, host, db), pool_pre_ping=True)
        if os.getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query all objects from the current database session."""

        # import all models to access them directly
        from models import base_model
        classes = [base_model.User, base_model.State, base_model.City,
                   base_model.Amenity, base_model.Place, base_model.Review]
        if cls:
            classes = [cls]
        objects = {}
        for cls in classes:
            query = self.__session.query(cls)
            for obj in query:
                key = f"{cls.__name__}.{obj.id}"
                objects[key] = obj
        return objects

    def new(self, obj):
        """Add the object to the current database session."""
        if obj:
            self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database session."""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete obj from the current database session."""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Create all tables and initialize session from the engine."""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
                bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()
