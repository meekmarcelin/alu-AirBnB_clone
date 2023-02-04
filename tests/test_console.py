#!/usr/bin/python3

import unittest
import models
from models.base_model import BaseModel
from models.user import User
from models import storage
import cmd

class TestHBNBCommand(unittest.TestCase):
    def setUp(self):
        self.hbnb = HBNBCommand()
        self.capturedOutput = io.StringIO()
        sys.stdout = self.capturedOutput

    def test_create(self):
        self.hbnb.onecmd("create BaseModel")
        model_id = self.capturedOutput.getvalue().strip()
        self.assertTrue(model_id in storage.all().keys())

        self.capturedOutput.truncate(0)
        self.capturedOutput.seek(0)

        self.hbnb.onecmd("create User")
        user_id = self.capturedOutput.getvalue().strip()
        self.assertTrue(user_id in storage.all().keys())

        self.capturedOutput.truncate(0)
        self.capturedOutput.seek(0)

        self.hbnb.onecmd("create ThisClassDoesntExist")
        output = self.capturedOutput.getvalue().strip()
        self.assertEqual(output, "** class doesn't exist **")

if __name__ == '__main__':
    unittest.main()
