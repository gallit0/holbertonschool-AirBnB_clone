#!/usr/bin/python3
"""Model base class"""


import uuid


from datetime import datetime


class BaseModel:
    """Base Model class"""

    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        """Return string of instance"""
        return f'[{self.__class__.__name__}] ({self.id}) <{self.__dict__}>'

    def save(self):
        """Saves update time"""
        self.updated_at = str(datetime.now())

    def to_dict(self):
        """To dicitonary function"""
        d = self.__dict__
        d['__class__'] = self.__class__.__name__
        return d
