#!/usr/bin/python3
"""unittest for Amenity"""

import unittest
from models.amenity import Amenity
from models import BaseModel

class TestAmenity(unittest.TestCase):
    """Test cases for Amenity class."""

    def setUp(self):
        """setup initializes an instance of a class and assigns it to self attribute"""
        self.a = Amenity()

    def test_user_inheritance(self):
        """test if Amenity is a subclass of BaseModel"""
        self.assertIsInstance(self.a, Amenity)

    def test_type(self):
        """tests if the type of the attribute is the correct one"""
        self.assertIsInstance(self.a.name, str)
    
if __name__ == "__main__":
    unittest.main()
