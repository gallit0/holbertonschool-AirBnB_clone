#!/usr/bin/python3
"""Model base class"""


import uuid


from datetime import *


class BaseModel:
    """Base Model class"""

    def __init__(self, *args, **kwargs):
        if kwargs:
            for i in kwargs:
                if i == 'id':
                    self.id = str(kwargs[i])
                if i == 'created_at':
                    t = datetime.strptime(kwargs[i], '%Y-%m-%dT%H:%M:%S.%f')
                    self.created_at = t
                if i == 'updated_at':
                    t = datetime.strptime(kwargs[i], '%Y-%m-%dT%H:%M:%S.%f')
                    self.updated_at = t
            return
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        """Return string of instance"""
        return f'[{self.__class__.__name__}] ({self.id}) <{self.__dict__}>'

    def save(self):
        """Saves update time"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """To dicitonary function"""
        d = self.__dict__
        d['__class__'] = self.__class__.__name__
        d['created_at'] = self.created_at.isoformat()
        d['updated_at'] = self.updated_at.isoformat()
        return d
