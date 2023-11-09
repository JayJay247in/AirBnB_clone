#!/usr/bin/python3
"""Module for storage initialization"""

from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City  
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage

classes = {
    "BaseModel": BaseModel,
    "User": User,
    "State": State,
    "City": City,
    "Amenity": Amenity,
    "Place": Place,
    "Review": Review
}

storage = FileStorage()
storage.reload()

if __name__ == "__main__":
    storage.reload()