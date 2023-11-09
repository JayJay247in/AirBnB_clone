#!/usr/bin/python3
import unittest
from models.state import State
from models.base_model import BaseModel

class TestState(unittest.TestCase):

    def test_inheritance(self):
        self.assertIsInstance(State(), BaseModel)

    def test_attributes(self):
        state = State()
        self.assertEqual(state.name, "")