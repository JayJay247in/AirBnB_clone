#!/usr/bin/python3
"""Test City module"""

import unittest

from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """Test cases for City model"""

    def test_inheritance(self):
        """Test inheritance from BaseModel"""
        self.assertIsInstance(City(), BaseModel)

    def test_attributes(self):
        """Test default attribute values"""
        c = City()
        self.assertEqual(c.state_id, "")
        self.assertEqual(c.name, "")

    def test_attr_types(self):
        """Test attribute types"""
        c = City()
        self.assertIsInstance(c.state_id, str)
        self.assertIsInstance(c.name, str)

    def test_setter(self):
        """Test setters update attributes"""
        c = City()
        c.state_id = "CA"
        c.name = "San Francisco"
        self.assertEqual(c.state_id, "CA")
        self.assertEqual(c.name, "San Francisco")


if __name__ == '__main__':
    unittest.main()