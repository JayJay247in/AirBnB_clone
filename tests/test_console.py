#!/usr/bin/python3
"""Test console module"""

import unittest
from unittest.mock import patch  
from io import StringIO

from console import HBNBCommand
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User


class TestConsole(unittest.TestCase):
    """Test cases for console"""

    @classmethod
    def setUpClass(cls):
        """Setup for test"""
        cls.mock_stdout = StringIO()

    def setUp(self):
        """Setup for each test"""
        self.console = HBNBCommand(stdout=self.mock_stdout)

    def tearDown(self):
        """Cleanup after each test"""
        self.mock_stdout.truncate(0)
        self.mock_stdout.seek(0)

    def get_output(self, cmd):
        """Helper to get output"""
        self.console.onecmd(cmd)
        return self.mock_stdout.getvalue()

    def test_create_user(self):
        """Test create user"""
        user_id = self.get_output("create User")
        self.assertIn("User." + user_id, FileStorage._FileStorage__objects)

    def test_show_user(self):
        """Test show user"""
        user_id = self.get_output("create User")
        user = self.get_output("show User " + user_id)
        self.assertIn("User." + user_id, user)

    def test_destroy_user(self):
        """Test destroy user"""
        user_id = self.get_output("create User")
        self.get_output("destroy User " + user_id)
        self.assertNotIn("User." + user_id, FileStorage._FileStorage__objects)
        
    def test_update_user(self):
        """Test update user"""
        user_id = self.get_output("create User")
        self.get_output("update User " + user_id + " email \"test@test.com\"")
        self.assertIn("test@test.com", str(FileStorage._FileStorage__objects["User." + user_id]))