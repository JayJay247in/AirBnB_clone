#!/usr/bin/python3
"""Test Place module"""

import unittest

from models.place import Place
from datetime import datetime
from models.base_model import BaseModel

class TestPlace(unittest.TestCase):
    """Test cases for Place class"""

    def test_inheritance(self):
        """Test inheritance from BaseModel"""
        self.assertIsInstance(Place(), BaseModel)

    def test_attributes(self):
        """Test attribute values"""
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
        """Test attribute types"""
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

    def test_setter(self):
        """Test setters update attributes"""
        p = Place()
        p.city_id = "SF"
        p.user_id = "1234"
        self.assertEqual(p.city_id, "SF")
        self.assertEqual(p.user_id, "1234")

    def test_to_dict(self):
        """Test conversion to dict"""
        p = Place()
        d = p.to_dict()
        self.assertEqual(d['__class__'], 'Place')
        self.assertIsInstance(d['created_at'], str)
        self.assertIsInstance(d['updated_at'], str)

    def test_from_dict(self):
        """Test initialization from dict"""
        d = {
            "id": "12345",
            "__class__": "Place",
            "city_id": "SF",
            "user_id": "1234",
        }
        p = Place(**d)
        self.assertEqual(p.id, "12345")
        self.assertEqual(p.city_id, "SF")

    def test_str_representation(self):
        """Test string representation"""
        dt = datetime.utcnow()
        p = Place(id="123", created_at=dt, updated_at=dt)
        self.assertIn("[Place] (123)", str(p))

if __name__ == '__main__':
    unittest.main()