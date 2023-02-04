#!/usr/bin/python3
"""unittest for Place"""

import unittest
from models.place import Place
from models import BaseModel


class TestPlace(unittest.TestCase):
    """Test cases for Place class."""

    def setUp(self):
        """setup initializes an instance of a class and assigns it to self attribute"""
        self.p = Place()

    def test_user_inheritance(self):
        """test if Place is a subclass of BaseModel"""
        self.assertIsInstance(self.p, Place)

    def test_type(self):
        """tests if the type of the attribute is the correct one"""
        self.assertIsInstance(self.p.city_id, str)
        self.assertIsInstance(self.p.user_id, str)
        self.assertIsInstance(self.p.name, str)
        self.assertIsInstance(self.p.description, str)
        self.assertIsInstance(self.p.number_rooms, int)
        self.assertIsInstance(self.p.number_bathrooms, int)
        self.assertIsInstance(self.p.max_guest, int)
        self.assertIsInstance(self.p.price_by_night, int)
        self.assertIsInstance(self.p.latitude, float)
        self.assertIsInstance(self.p.longitude, float)
        self.assertIsInstance(self.p.amenity_ids, list)
    
if __name__ == "__main__":
    unittest.main()
