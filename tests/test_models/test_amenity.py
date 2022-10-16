#!/usr/bin/python3
""" base model tests """
from lib2to3.pytree import Base
import unittest
from models.amenity import Amenity

class BaseModelClass(unittest.TestCase):
    """ Test basemodel """
    def test_city(self):
        inst = Amenity()
        self.assertEqual(inst.name, '')
