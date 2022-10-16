#!/usr/bin/python3
""" base model tests """
from lib2to3.pytree import Base
import unittest
from models.review import Review

class BaseModelClass(unittest.TestCase):
    """ Test basemodel """
    def test_city(self):
        inst = Review()
        self.assertEqual(inst.place_id, '')
        self.assertEqual(inst.user_id, '')
        self.assertEqual(inst.text, '')
