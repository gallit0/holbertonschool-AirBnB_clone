#!/usr/bin/python3
"""File storage"""


import json


import models


class FileStorage:
    """File Storage class"""
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Returns dictionary"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects"""
        name = obj.__class__.__name__ + '.' + obj.id
        FileStorage.__objects[name] = obj.to_dict()

    def save(self):
        """Serializes"""
        with open(FileStorage.__file_path, 'w') as f:
            f.write(json.dumps(FileStorage.__objects, default=str))

    def reload(self):
        """Deserializes"""
        try:
            with open(self.__file_path, 'r') as f:
                d = json.load(f)
                FileStorage.__objects = d
                for key, value in d.items:
                    self.new(eval(value['__class__'])(**value))
        except:
            pass
