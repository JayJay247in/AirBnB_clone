#!/usr/bin/python3
"""Test BaseModel module"""

import unittest
from models.base_model import BaseModel


class TestBaseModelInit(unittest.TestCase):
    """Tests for BaseModel initialization"""

    def test_init_with_kwargs(self):
        """Test init with kwargs"""
        d = {
            "id": "56d43177-cc5f-4d6c-a0c1-e167f8c27337",
            "created_at": "2017-09-28T21:03:54.052298",
            "__class__": "BaseModel",
            "my_number": 89,
            "updated_at": "2017-09-28T21:03:54.052302",
            "name": "My_First_Model"
        }
        m = BaseModel(**d)
        self.assertEqual(m.id, d["id"])
        self.assertEqual(m.created_at.isoformat(), d["created_at"])


if __name__ == '__main__':
    unittest.main()