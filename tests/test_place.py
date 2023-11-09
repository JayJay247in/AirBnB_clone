#!/usr/bin/python3
import unittest
from models.place import Place
from models.base_model import BaseModel

class TestPlace(unittest.TestCase):

    def test_inheritance(self):
        self.assertIsInstance(Place(), BaseModel)

    def test_attributes(self):
        p = Place()
        self.assertEqual(p.city_id, "")
        self.assertEqual(p.user_id, "")
        self.assertEqual(p.name, "")
        self.assertEqual(p.description, "")
        self.assertEqual(p.number_rooms, 0)
        self.assertEqual(p.number_bathrooms, 0)
        self.assertEqual(p.max_guest, 0)
        self.assertEqual(p.price_by_night, 0)
        self.assertEqual(p.latitude, 0.0)
        self.assertEqual(p.longitude, 0.0)
        self.assertEqual(p.amenity_ids, [])

    def test_attr_types(self):
        p = Place()
        self.assertIsInstance(p.city_id, str)
        self.assertIsInstance(p.user_id, str)
        self.assertIsInstance(p.name, str)
        self.assertIsInstance(p.description, str)
        self.assertIsInstance(p.number_rooms, int)
        self.assertIsInstance(p.number_bathrooms, int)
        self.assertIsInstance(p.max_guest, int)
        self.assertIsInstance(p.price_by_night, int)
        self.assertIsInstance(p.latitude, float)
        self.assertIsInstance(p.longitude, float)
        self.assertIsInstance(p.amenity_ids, list)

    # Further tests...

if __name__ == '__main__':
    unittest.main()