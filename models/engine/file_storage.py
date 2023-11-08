import json
from models.base_model import BaseModel
from models.user import User

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        with open(FileStorage.__file_path, "w") as f:
            d = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
            json.dump(d, f)

    def reload(self):
        try:
            with open(FileStorage.__file_path) as f:
                FileStorage.__objects = {}
                temp = json.load(f)
                for k, v in temp.items():
                    cls_name = v["__class__"]
                    del v["__class__"]
                    FileStorage.__objects[k] = eval(cls_name)(**v)
        except FileNotFoundError:
            pass
    
    def __init__(self):
        self.all()

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
                for cls in store.keys():
                    if cls == "BaseModel":
                        for k, v in store[cls].items():
                            obj = BaseModel(**v)
                            FileStorage.__objects[cls + '.' + k] = obj
                    elif cls == "User":
                        for k, v in store[cls].items():
                            obj = User(**v)
                            FileStorage.__objects[cls + '.' + k] = obj
        except:
            pass