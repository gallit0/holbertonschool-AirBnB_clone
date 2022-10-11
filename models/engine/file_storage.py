#!/usr/bin/python3
"""File storage"""


import json





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
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as f:
                d = json.loads(f.read())
                name = ''
                from models import BaseModel
                for i in d:
                    BaseModel(d[i])
        except:
            pass
