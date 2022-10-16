#!/usr/bin/python3
""" file storage tests """
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

class FileStorageClass(unittest.TestCase):
    """ Test File Storage """

    def test_filepath(self):
        """
        Checks that the file path is set to file.json
        """
        f = FileStorage()
        a = f._FileStorage__file_path
        self.assertEqual(a, "file.json")

    def test_objects(self):
        obj = FileStorage()
        self.assertEqual(type(obj._FileStorage__objects), dict)

    def test_all(self):
        obj = FileStorage()
        self.assertEqual(obj.all(), {})

    def test_new(self):
        f = FileStorage()
        obj = BaseModel()
        self.assertEqual(f.new(obj), None)
        self.assertEqual(f._FileStorage__objects, f.all())
        
    def test_save(self):
        f = FileStorage()
        self.assertEqual(f.save(), None)

    def test_reload(self):
        f = FileStorage()
        self.assertEqual(f.reload(), None)
