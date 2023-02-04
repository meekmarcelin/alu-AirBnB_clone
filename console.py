#!/usr/bin/python3
""" it's all about console """


import cmd
import models

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program\n"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program\n"""
        return True

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id\n"""
        pass

    def do_show(self, arg):
        """Prints the string representation of an instance based on the class name and id\n"""
        pass

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id (save the change into the JSON file)\n"""
        pass

    def do_all(self, arg):
        """Prints all string representation of all instances based or not on the class name\n"""
        pass

    def do_update(self, arg):
        """Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file)\n"""
        pass

    def emptyline(self):
        """Called when an empty line is entered in response to the prompt. If this method is not overridden, it repeats the last non-empty command entered.\n"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
