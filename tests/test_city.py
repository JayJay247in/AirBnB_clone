import unittest
from models.city import City
from models.base_model import BaseModel

class TestCity(unittest.TestCase):

    def test_inheritance(self):
        self.assertIsInstance(City(), BaseModel)

    def test_attributes(self):
        c = City()
        self.assertEqual(c.state_id, "")
        self.assertEqual(c.name, "")

    def test_attr_types(self):
        c = City()
        self.assertIsInstance(c.state_id, str)
        self.assertIsInstance(c.name, str)

    def test_setter(self):
        c = City()
        c.state_id = "CA"
        c.name = "San Francisco"
        self.assertEqual(c.state_id, "CA")
        self.assertEqual(c.name, "San Francisco")

if __name__ == '__main__':
    unittest.main()