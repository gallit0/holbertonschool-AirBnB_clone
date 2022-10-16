#!/usr/bin/python3
""" base model tests """
from lib2to3.pytree import Base
import unittest
from models.user import User

class BaseModelClass(unittest.TestCase):
    """ Test basemodel """
    """def test_id(self):
        att = BaseModel()
        result = att.id
        res2 = result
        self.assertEqual(result, res2)

    def test_save(self):
        inst = BaseModel()
        first_res = inst.updated_at
        inst.save()
        save_res = inst.updated_at
        self.assertNotEqual(first_res, save_res)

    def test_str(self):
        inst = BaseModel()
        res = f'[{inst.__class__.__name__}] ({inst.id}) <{inst.__dict__}>'
        self.assertEqual(res, str(inst))
    """
    def test_userEmail(self):
        inst = User()
        self.assertEqual(inst.email, '')
