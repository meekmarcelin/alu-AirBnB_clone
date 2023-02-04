#test/user.py
#!/usr/bin/python3
"""unittest for User"""

import unittest
from models.user import User
from models import BaseModel


class TestUser(unittest.TestCase):
    """Test cases for User class."""

    def setUp(self):
        """setup initializes an instance of a class and assigns it to self attribute"""
        self.u = User()

    def test_user_inheritance(self):
        """test if User is a subclass of BaseModel"""
        self.assertIsInstance(self.u, User)

    def test_type(self):
        """tests if the type of the attribute is the correct one"""
        self.assertIsInstance(self.u.email, str)
        self.assertIsInstance(self.u.password, str)
        self.assertIsInstance(self.u.first_name, str)
        self.assertIsInstance(self.u.last_name, str)
        
    
if __name__ == "__main__":
    unittest.main()
