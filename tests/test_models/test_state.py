#!/usr/bin/python3
"""unittest for state"""

import unittest
from models.state import State
from models import BaseModel

class TestState(unittest.TestCase):
    """Test cases for State class."""

    def setUp(self):
        """setup initializes an instance of a class and assigns it to self attribute"""
        self.s = State()

    def test_user_inheritance(self):
        """test if State is a subclass of BaseModel"""
        self.assertIsInstance(self.s, State)

    def test_type(self):
        """tests if the type of the attribute is the correct one"""
        self.assertIsInstance(self.s.name, str)
    
if __name__ == "__main__":
    unittest.main()
