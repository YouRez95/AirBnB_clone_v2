#!/usr/bin/python3
"""Module - Database Storing Engine"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models.place import Place
from models.base_model import Base
from os import getenv


class DBStorage:
    """This class manages the database storage for HBNB_clone project
    """
    __engine = None
    __session = None

    def __init__(self):
        """Initilizes database conncection
        """
        HBNB_MYSQL_USER = getenv('HBNB_MYSQL_USER')
        HBNB_MYSQL_PWD = getenv('HBNB_MYSQL_PWD')
        HBNB_MYSQL_HOST = getenv('HBNB_MYSQL_HOST')
        HBNB_MYSQL_DB = getenv('HBNB_MYSQL_DB')
        HBNB_ENV = getenv('HBNB_ENV')

        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'.format(
                HBNB_MYSQL_USER,
                HBNB_MYSQL_PWD,
                HBNB_MYSQL_HOST,
                HBNB_MYSQL_DB
            ),
            pool_pre_ping=True
        )
        if HBNB_ENV == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Queries all objects from the database
        """
        obj_dict = {}

        if cls:
            data = self.__session.query(cls).all()
        else:
            hbnb_classes = [City, State, User, Place, Review, Amenity]
            data = []
            for hc in hbnb_classes:
                data.extend(self.__session.query(hc).all())

        for obj in data:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            obj_dict[key] = obj

        return obj_dict

    def new(self, obj):
        """Adds a new obj to the current database session
        """
        self.__session.add(obj)

    def save(self):
        """Commits all changes of the current database session
        """
        self.__session.commit()

    def delete(self, obj=None):
        """Deletes obj from the current database session
        """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Creates all tables in the database"""
        Base.metadata.create_all(self.__engine)
        current_db_session = sessionmaker(
            bind=self.__engine,
            expire_on_commit=False
        )
        DBStorage.__session = scoped_session(current_db_session)

    def close(self):
        self.__session.remove()
