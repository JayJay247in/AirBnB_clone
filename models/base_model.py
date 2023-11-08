import uuid
from datetime import datetime
from models import storage

class BaseModel:

    def __init__(self, *args, **kwargs):
        """Initialize instance attributes"""
        if kwargs:
            # Instantiate with kwargs dict
            for key, value in kwargs.items():
                if key != "__class__":
                    if key in ("created_at", "updated_at"):
                        value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, value)
        else:
            # New instance, set defaults 
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at

    def __str__(self):
        return "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        dictionary = self.__dict__.copy()
        dictionary["__class__"] = type(self).__name__ 
        dictionary["created_at"] = self.created_at.isoformat()
        dictionary["updated_at"] = self.updated_at.isoformat()
        return dictionary

    def __init__(self, *args, **kwargs):
        #...
        if not kwargs:
            storage.new(self)

    def save(self):
        #...
        storage.save()