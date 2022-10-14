#!/usr/bin/python3
""" file storage tests """
import unittest
from models.engine.file_storage import FileStorage
import os


class FileStorageClass(unittest.TestCase):
    """ Test File Storage """
    def test_filepath(self):
        obj = FileStorage()
        self.assertEqual(obj._FileStorage__file_path, "file.json")
