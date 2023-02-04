#!/usr/bin/python3
"""Unit test for the BaseModel class"""

import unittest
import datetime
from models import BaseModel

class TestBaseModel(unittest.TestCase):
    """Tests for the public attributes and methods of the BaseModel class"""

    def setUp(self):
        """Create an instance of the BaseModel class for testing"""
        self.base_model = BaseModel()

    def test_type(self):
        """Test the type of the BaseModel instance and its to_dict method"""
        self.base_model.save()
        base_model_dict = self.base_model.to_dict()

        self.assertEqual(self.base_model.name, base_model_dict['name'])
        self.assertEqual(self.base_model.my_number, base_model_dict['my_number'])
        self.assertEqual('BaseModel', base_model_dict['__class__'])
        self.assertEqual(self.base_model.id, base_model_dict['id'])

    def test_save(self):
        """Test the behavior of the save method and the id, created_at, and updated_at attributes"""
        self.base_model.first_name = "First"
        self.base_model.save()

        self.assertIsInstance(self.base_model.id, str)
        self.assertIsInstance(self.base_model.created_at, datetime.datetime)
        self.assertIsInstance(self.base_model.updated_at, datetime.datetime)

        first_dict = self.base_model.to_dict()

        self.base_model.first_name = "Second"
        self.base_model.save()
        second_dict = self.base_model.to_dict()

        self.assertEqual(first_dict['created_at'], second_dict['created_at'])
        self.assertNotEqual(first_dict['updated_at'], second_dict['updated_at'])

if __name__ == "__main__":
    unittest.main()
