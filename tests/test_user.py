#!/usr/bin/python3
"""Test User module"""

import unittest

from models.base_model import BaseModel
from models.user import User


class TestUser(unittest.TestCase):
    """Test cases for User class"""

    def test_inheritance(self):
        """Test inheritance from BaseModel"""
        self.assertIsInstance(User(), BaseModel)

    def test_attributes(self):
        """Test default attribute values"""
        user = User()
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")

    def test_setter(self):
        """Test setters update attributes"""
        user = User()
        user.email = "test@example.com"
        user.password = "password"
        user.first_name = "John"
        user.last_name = "Doe"
        self.assertEqual(user.email, "test@example.com")
        self.assertEqual(user.password, "password")
        self.assertEqual(user.first_name, "John")
        self.assertEqual(user.last_name, "Doe")


if __name__ == '__main__':
    unittest.main()