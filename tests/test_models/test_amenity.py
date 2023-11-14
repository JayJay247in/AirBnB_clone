#!/usr/bin/python3
"""Test Amenity module"""

import unittest

from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """Test cases for Amenity model"""

    def test_inheritance(self):
        """Test inheritance from BaseModel"""
        self.assertIsInstance(Amenity(), BaseModel)

    def test_attributes(self):
        """Test default attribute values"""
        a = Amenity()
        self.assertEqual(a.name, "")

    def test_attr_types(self):
        """Test attribute types"""
        a = Amenity()
        self.assertIsInstance(a.name, str)

    def test_setter(self):
        """Test name setter"""
        a = Amenity()
        a.name = "Wifi"
        self.assertEqual(a.name, "Wifi")

    def test_to_dict(self):
        """Test conversion to dict"""
        a = Amenity()
        d = a.to_dict()
        self.assertEqual(d['__class__'], 'Amenity')
        self.assertIsInstance(d['created_at'], str)
        self.assertIsInstance(d['updated_at'], str)


if __name__ == '__main__':
    unittest.main()