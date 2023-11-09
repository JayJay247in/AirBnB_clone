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

    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        cls = obj.__class__.__name__
        FileStorage.__objects[cls + "." + obj.id] = obj

    def save(self):
        store = {}
        for k, v in FileStorage.__objects.items():
            cls = k.split('.')[0]
            if cls not in store:
                store[cls] = {} 
            store[cls][k.split('.')[1]] = v.to_dict()

        with open(FileStorage.__file_path, 'w') as f:
            json.dump(store, f)

    def reload(self):
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