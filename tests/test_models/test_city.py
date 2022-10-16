#!/usr/bin/python3
""" base model tests """
from lib2to3.pytree import Base
import unittest
from models.city import City

class BaseModelClass(unittest.TestCase):
    """ Test basemodel """
    def test_city(self):
        inst = City()
        self.assertEqual(inst.name, '')
        self.assertEqual(inst.state_id, '')
