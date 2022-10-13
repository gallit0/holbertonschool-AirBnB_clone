#!/usr/bin/python3
""" base model tests """
import unittest
from models.base_model import BaseModel

class BaseModelClass(unittest.TestCase):
    """ Test basemodel """
    def test_save_empty(self):
        att = BaseModel()
        result = att.id
        res2 = result
        self.assertEqual(result, res2)
