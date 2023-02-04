#!/usr/bin/python3
""" storage """


import json
from datetime import datetime
from models.base_model import BaseModel

class FileStorage:
    """ store the files """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        key = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            d = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
            f.write(json.dumps(d))

    def reload(self):
        try:
            with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
                FileStorage.__objects = {k: BaseModel(**v) for k, v in json.loads(f.read()).items()}
        except FileNotFoundError:
            pass
