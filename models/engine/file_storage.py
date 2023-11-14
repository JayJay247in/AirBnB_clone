#!/usr/bin/python3
"""File storage module"""

import json

from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place  
from models.review import Review

classes = {
    "BaseModel": BaseModel,
    "User": User,
    "State": State,
    "City": City,
    "Amenity": Amenity,
    "Place": Place,
    "Review": Review
}


class FileStorage:
    """Class for file storage"""

    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        if cls:
            objects = {}
            for key, obj in FileStorage.__objects.items():
                if type(obj).__name__ == cls.__name__:
                    objects[key] = obj
            return objects
        else:
            return FileStorage.__objects

    def count(self, cls=None):
        count = 0
        if cls:
            for obj in FileStorage.__objects.values():
                if type(obj).__name__ == cls.__name__:
                    count += 1
        else:
            count = len(FileStorage.__objects)
        return count

    def new(self, obj):
        """Sets object in __objects dict"""
        cls = obj.__class__.__name__
        FileStorage.__objects[cls + "." + obj.id] = obj

    def save(self):
        """Serializes __objects to JSON file"""
        store = {}
        for k, v in FileStorage.__objects.items():
            cls = k.split('.')[0]
            if cls not in store:
                store[cls] = {}
            store[cls][k.split('.')[1]] = v.to_dict()

        with open(FileStorage.__file_path, 'w') as f:
            json.dump(store, f)

    def reload(self):
        """Deserializes JSON file to __objects"""
        try:
            with open(FileStorage.__file_path) as f:
                FileStorage.__objects = {}
                store = json.load(f)
                for cls in classes.values():
                    if cls.__name__ in store:
                        for k, v in store[cls.__name__].items():
                            obj = cls(**v)
                            FileStorage.__objects[cls.__name__ + '.' + k] = obj
        except:
            pass