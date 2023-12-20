#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from models import HBNB_TYPE_STORAGE

Base = declarative_base()


class BaseModel:
    """A base class for all hbnb models"""

    __abstract__ = True

    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            kwargs['created_at'] = datetime.strptime(
                kwargs.get('created_at', datetime.utcnow())
                .strftime('%Y-%m-%dT%H:%M:%S.%f'), '%Y-%m-%dT%H:%M:%S.%f')
            kwargs['updated_at'] = datetime.strptime(
                kwargs.get('updated_at', datetime.utcnow())
                .strftime('%Y-%m-%dT%H:%M:%S.%f'), '%Y-%m-%dT%H:%M:%S.%f')

            kwargs.pop('__class__', None)
            self.__dict__.update(kwargs)

            for key, value in kwargs.items():
                if not hasattr(self, key):
                    setattr(self, key, value)
            if HBNB_TYPE_STORAGE == 'db':
                if not hasattr(kwargs, 'id'):
                    setattr(self, 'id', str(uuid.uuid4()))

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()

        dictionary.pop('_sa_instance_state', None)

        return dictionary

    def delete(self):
        """Deletes the current instance from the storage"""
        from models import storage
        storage.delete(self)
