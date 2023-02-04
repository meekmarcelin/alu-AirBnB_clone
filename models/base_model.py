#!/usr/bin/python3
"""
Base_model module
"""

import uuid
from datetime import datetime
from models import storage

def __init__(self, *args, **kwargs):
    if kwargs:
        kwargs.pop("__class__", None)
        for key, value in kwargs.items():
            setattr(self, key, value)

        if "created_at" in kwargs:
            self.created_at = datetime.strptime(kwargs["created_at"],
                                                "%Y-%m-%dT%H:%M:%S.%f")
        if "updated_at" in kwargs:
            self.updated_at = datetime.strptime(kwargs["updated_at"],
                                                "%Y-%m-%dT%H:%M:%S.%f")
    else:
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        storage.new(self)

 def __str__(self):
        return "[{}] ({}) {}".format(
            type(self).__name__, self.id, self.__dict__)

 def save(self):
        self.updated_at = datetime.now()
        storage.save()

 def to_dict(self):
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = type(self).__name__
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        return new_dict
