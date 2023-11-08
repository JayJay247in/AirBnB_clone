import console
import unittest
from models.base_model import BaseModel
from models import storage
from models import User

def test_create_user(self):
    console.do_create("User")
    user_id = capture_output() # id printed
    self.assertIn("User." + user_id, storage.all())