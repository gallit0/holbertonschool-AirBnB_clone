#!/usr/bin/python3
""" base model tests """
from lib2to3.pytree import Base
import unittest
from models.base_model import BaseModel

class BaseModelClass(unittest.TestCase):
    """ Test basemodel """
    def test_save(self):
        inst = BaseModel()
        cr = inst.created_at
        up = inst.updated_at
        inst.save()
        self.assertEqual(cr, inst.created_at)
        self.assertNotEqual(up, inst.updated_at)

    def test_to_dict(self):
        inst = BaseModel()
        d = inst.to_dict()
        self.assertEqual(inst.to_dict(), dict(d))

    def test_string(self):
        self.assertEqual(str, type(str(BaseModel)))
