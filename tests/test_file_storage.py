#!/usr/bin/python3
"""Test FileStorage module"""

import unittest
from models.base_model import BaseModel
from models import storage


class TestFileStorage(unittest.TestCase):
    """Tests for FileStorage class"""

    def test_attributes(self):
        """Test class attributes"""
        self.assertEqual(storage._FileStorage__objects, {})
        self.assertEqual(storage._FileStorage__file_path, "file.json")

    def test_all(self):
        """Test all method"""
        m = BaseModel()
        key = "{}.{}".format(m.__class__.__name__, m.id)
        storage.new(m)
        self.assertDictEqual(storage.all(), {key: m})

    def test_serialization(self):
        """Test serialization of objects"""
        user = User()
        user.save()
        store = storage.all()
        self.assertIsInstance(store["User." + user.id], User)


if __name__ == '__main__':
    unittest.main()