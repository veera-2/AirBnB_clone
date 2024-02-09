#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
import datetime

my_model = BaseModel()
my_model.name = "My First Model"
my_model.my_number = 89
print(my_model)
my_model.save()
print(my_model)
my_model_json = my_model.to_dict()
print(my_model_json)
print("JSON of my_model:")
for key in my_model_json.keys():
    print(("\t{}: ({}) - {}"
          .format(key, type(my_model_json[key]), my_model_json[key])))

class TestBaseModel(unittest.TestCase):
    """
    Test cases for the BaseModel class.
    """

    def test_init(self):
        """
        Test the __init__ method of the BaseModel class.
        """
        # Test __init__ method
        base_model = BaseModel()
        self.assertTrue(hasattr(base_model, 'id'))
        self.assertTrue(hasattr(base_model, 'created_at'))
        self.assertTrue(hasattr(base_model, 'updated_at'))
        self.assertIsInstance(base_model.created_at, datetime.datetime)
        self.assertIsInstance(base_model.updated_at, datetime.datetime)

    def test_str(self):
        """
        Test the __str__ method of the BaseModel class.
        """
        # Test __str__ method
        base_model = BaseModel()
        expected_str = "[BaseModel] ({}) {}".format(base_model.id, base_model.__dict__)
        self.assertEqual(str(base_model), expected_str)

    def test_save(self):
        """
        Test the save method of the BaseModel class.
        """
        # Test save method
        base_model = BaseModel()
        initial_updated_at = base_model.updated_at
        base_model.save()
        self.assertNotEqual(base_model.updated_at, initial_updated_at)

    def test_to_dict(self):
        """
        Test the to_dict method of the BaseModel class.
        """
        # Test to_dict method
        base_model = BaseModel()
        obj_dict = base_model.to_dict()
        self.assertTrue(isinstance(obj_dict, dict))
        self.assertTrue('id' in obj_dict)
        self.assertTrue('created_at' in obj_dict)
        self.assertTrue('updated_at' in obj_dict)
        self.assertTrue('__class__' in obj_dict)

if __name__ == '__main__':
    unittest.main()
