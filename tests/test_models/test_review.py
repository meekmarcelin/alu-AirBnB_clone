#!/usr/bin/python3
"""unittest for Review """

import unittest
from models.review import Review
from models import BaseModel


class TestReview(unittest.TestCase):
    """Test cases for Review class."""

    def setUp(self):
        """setup initializes an instance of a class and assigns it to self attribute"""
        self.r = Review()

    def test_user_inheritance(self):
        """test if Review is a subclass of BaseModel"""
        self.assertIsInstance(self.r, Review)

    def test_type(self):
        """tests if the type of the attribute is the correct one"""
        self.assertIsInstance(self.r.place_id, str)
        self.assertIsInstance(self.r.user_id, str)
        self.assertIsInstance(self.r.text, str)
    
if __name__ == "__main__":
    unittest.main()
