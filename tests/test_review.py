import unittest
from models.review import Review
from models.base_model import BaseModel

class TestReview(unittest.TestCase):

    def test_inheritance(self):
        self.assertIsInstance(Review(), BaseModel)

    def test_attributes(self):
        r = Review()
        self.assertEqual(r.place_id, "")
        self.assertEqual(r.user_id, "")
        self.assertEqual(r.text, "")

    def test_attr_types(self):
        r = Review()
        self.assertIsInstance(r.place_id, str)
        self.assertIsInstance(r.user_id, str)
        self.assertIsInstance(r.text, str)

    def test_setter(self):
        r = Review()
        r.place_id = "123"
        r.user_id = "456"
        r.text = "Great place!"
        self.assertEqual(r.place_id, "123")
        self.assertEqual(r.user_id, "456")
        self.assertEqual(r.text, "Great place!")

    def test_to_dict(self):
        r = Review()
        d = r.to_dict()
        self.assertEqual(d['__class__'], 'Review')
        self.assertIsInstance(d['created_at'], str)
        self.assertIsInstance(d['updated_at'], str)

if __name__ == '__main__':
    unittest.main()