#!/usr/bin/python3
""" Amenity testing """
import unittest
import pep8
from models.amenity import Amenity

class Amenity_testing(unittest.TestCase):
    """ checks BaseModel """

    def testpep8(self):
        """ testing codestyle """
        pep_stylecode = pep8.StyleGuide(quiet=True)
        path_user = 'models/amenity.py'
        result = pep_stylecode.check_files([path_user])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")
