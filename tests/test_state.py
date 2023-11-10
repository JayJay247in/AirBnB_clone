#!/usr/bin/python3
"""Test State module"""

import unittest

from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """Test cases for State class"""

    def test_inheritance(self):
        """Test inheritance from BaseModel"""
        self.assertIsInstance(State(), BaseModel)

    def test_attributes(self):
        """Test default attribute values"""
        state = State()
        self.assertEqual(state.name, "")


if __name__ == '__main__':
    unittest.main()