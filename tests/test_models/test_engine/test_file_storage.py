#!/usr/bin/python3
""" file storage tests """
import unittest
from models.engine.file_storage import FileStorage


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
