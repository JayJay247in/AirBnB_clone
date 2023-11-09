#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from models import storage
from models import User

class TestFileStorage(unittest.TestCase):

    def test_attributes(self):
        self.assertEqual(storage._FileStorage__objects, {})
        self.assertEqual(storage._FileStorage__file_path, "file.json")

    def test_all(self):
        m = BaseModel()
        key = "{}.{}".format(m.__class__.__name__, m.id)
        storage.new(m)
        self.assertDictEqual(storage.all(), {key: m})

    def test_serialization(self):
        user = User()
        user.save()
        store = storage.all()
        self.assertIsInstance(store["User." + user.id], User)
if __name__ == '__main__':
    unittest.main()