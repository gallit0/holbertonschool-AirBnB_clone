#!/usr/bin/python3
""" base model tests """
from lib2to3.pytree import Base
import unittest
from models.place import Place

class BaseModelClass(unittest.TestCase):
    """ Test basemodel """
    def test_city(self):
        inst = Place()
        self.assertEqual(inst.name, '')
        self.assertEqual(inst.city_id, '')
        self.assertEqual(inst.user_id, '')
        self.assertEqual(inst.description, '')
        self.assertEqual(inst.number_rooms, 0)
        self.assertEqual(inst.number_bathrooms, 0)
        self.assertEqual(inst.max_guest, 0)
        self.assertEqual(inst.price_by_night, 0)
        self.assertEqual(inst.latitude, 0.0)
        self.assertEqual(inst.longitude, 0.0)
        self.assertEqual(inst.amenity_ids, [])
