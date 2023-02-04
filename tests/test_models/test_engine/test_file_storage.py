#!/usr/bin/python3
"""Unit test for file storage"""

import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import os

class TestFileStorage(unittest.TestCase):

    def setUp(self):
        """Create an instance of the class for testing"""
        self.base_model = BaseModel()
        self.store = FileStorage()
    
    def setUp(self):
        """ condition to test file saving """
        with open("test.json", 'w'):
            FileStorage._FileStorage__file_path = "test.json"
            FileStorage._FileStorage__objects = {}

    def reset_file(self):
        """Resets file path and deletes test file if it exists"""
        FileStorage._FileStorage__file_path = "file.json"
        try:
            os.remove("test.json")
        except FileNotFoundError:
            pass

    def test_reload(self):
        """test if reload """
        self.store.new(self.base_model)
        self.store.save()
        original_dict = self.store.all()
        os.remove("test.json")
        self.store.reload()
        reloaded_dict = self.store.all()
        self.assertDictEqual(original_dict, reloaded_dict)

    def test_save(self):
        """ Check save to file storage """
        self.store.new(self.base_model)
        original_dict = self.store.all()
        self.store.save()
        self.store.reload()
        reloaded_dict = self.store.all()
        self.assertDictEqual(original_dict, reloaded_dict)

if __name__ == '__main__':
    unittest.main()
