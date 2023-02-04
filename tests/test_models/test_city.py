#!/usr/bin/python3
"""unittest for city"""

import unittest
from models.city import City
from models import BaseModel

class TestCity(unittest.TestCase):
    """Test cases for City class."""

    def setUp(self):
        """setup initializes an instance of a class and assigns it to self attribute"""
        self.c = City()

    def test_user_inheritance(self):
        """test if City is a subclass of BaseModel"""
        self.assertTrue(self.c, City)

    def test_type(self):
        """tests if the type of the attribute is the correct one"""
        self.assertIsInstance(self.c.name, str)
        self.assertIsInstance(self.c.state_id, str)
    
if __name__ == "__main__":
    unittest.main()
