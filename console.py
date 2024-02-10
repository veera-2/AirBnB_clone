#!/usr/bin/python3
""" Console Module """
import cmd
import sys
import re
import os
from datetime import datetime
import uuid
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

class HBNBCommand(cmd.Cmd):
    """Contains the functionality for the HBNB console"""

    prompt = '(hbnb) ' if sys.__stdin__.isatty() else ''
    classes = {
        'BaseModel': BaseModel, 'User': User, 'Place': Place,
        'State': State, 'City': City, 'Amenity': Amenity,
        'Review': Review
    }
    dot_cmds = ['all', 'count', 'show', 'destroy', 'update']
    types = {
        'number_rooms': int, 'number_bathrooms': int,
        'max_guest': int, 'price_by_night': int,
        'latitude': float, 'longitude': float
    }

    def preloop(self):
        """Prints if isatty is false"""
        if not sys.__stdin__.isatty():
            print('(hbnb)')

    def precmd(self, line):
        """Reformat command line for advanced command syntax."""
        # ... (unchanged)

    def postcmd(self, stop, line):
        """Prints if isatty is false"""
        if not sys.__stdin__.isatty():
            print('(hbnb) ', end='')
        return stop

    # ... (unchanged)

    def do_create(self, args):
        """Create an object of any class"""
        # ... (unchanged)

    def do_show(self, args):
        """Method to show an individual object"""
        # ... (unchanged)

    def do_destroy(self, args):
        """Destroys a specified object"""
        # ... (unchanged)

    def do_all(self, args):
        """Shows all objects, or all objects of a class"""
        # ... (unchanged)

    def do_count(self, args):
        """Count current number of class instances"""
        # ... (unchanged)

    def do_update(self, args):
        """Updates a certain object with new info"""
        # ... (unchanged)


if __name__ == "__main__":
    HBNBCommand().cmdloop()

