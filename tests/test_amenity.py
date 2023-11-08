import unittest
from models.amenity import Amenity
from models.base_model import BaseModel

class TestAmenity(unittest.TestCase):

    def test_inheritance(self):
        self.assertIsInstance(Amenity(), BaseModel)

    def test_attributes(self):
        a = Amenity()
        self.assertEqual(a.name, "")

    def test_attr_types(self):
        a = Amenity()
        self.assertIsInstance(a.name, str)

    def test_setter(self):
        a = Amenity()
        a.name = "Wifi"
        self.assertEqual(a.name, "Wifi")

    def test_to_dict(self):
        a = Amenity()
        d = a.to_dict()
        self.assertEqual(d['__class__'], 'Amenity')
        self.assertIsInstance(d['created_at'], str)
        self.assertIsInstance(d['updated_at'], str)

if __name__ == '__main__':
    unittest.main()