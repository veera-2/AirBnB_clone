#!/usr/bin/python3
import uuid
import datetime
import json

"""
A class called BaseModel
"""


class BaseModel:
    def __init__(self, *args, **kwargs):
        if kwargs:
            # Initialize object attributes from dictionary representation
            ...
        else:
            # Create new instance
            ...
            storage.new(self)

    def save(self, storage_instance):
        """
        Updates the attribute 'updated_at' with the current datetime
        and saves the object to the storage.
        """
        self.updated_at = datetime.datetime.now()
        storage_instance.save()


class BaseModel:
    """
    A BaseModel class that defines common attributes/methods for other classes.
    """
    def __init__(self, *args, **kwargs):
        """
        Initializes a BaseModel instance.

        Args:
            *args: Variable length argument list (not used).
            **kwargs: Arbitrary keyword arguments.

        If kwargs is not empty:
            - Each key of this dictionary is an attribute name
            (Note __class__ from kwargs is not added as an attribute).
            - Each value of this dictionary is the
            value of the corresponding attribute.
            - Convert created_at and updated_at strings into datetime objects.
        Otherwise:
            - Create id and created_at as previously (new instance).
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue  # Skip __class__ attribute
                elif key in ('created_at', 'updated_at'):
                    formatted_date = (datetime.datetime.strptime
                                      (value, "%Y-%m-%dT%H:%M:%S.%f"))
                else:
                    setattr(self, key, formatted_date)
        else:
            self.created_at = datetime.datetime.now()
            self.updated_at = self.created_at
            self.name = getattr(self, 'name', None)
            self.id = str(uuid.uuid4())

    def __str__(self):
        """
        Converts the BaseModel instance to string representation.
        """
        return ("[{}] ({}) {}"
                .format(type(self).__name__, self.id, self.__dict__))

    def save(self):
        """
        Updates the attribute 'updated_at' with the current datetime.
        """
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of the instance.
        """
        obj_dict = {
            'my_number': getattr(self, 'my_number', None),
            'name': getattr(self, 'name', None),
            '__class__': type(self).__name__,
            'updated_at': self.updated_at.isoformat(),
            'id': self.id,
            'created_at': self.created_at.isoformat()
        }
        return obj_dict
