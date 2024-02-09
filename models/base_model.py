#!/usr/bin/python3
import uuid
import datetime
import json
"""
A class called BaseModel
"""


class BaseModel:
    """
    A BaseModel class that defines common attributes/methods for other classes.
    """
    def __init__(self):
        """
        Initializes a BaseModel instance with id,
        when it was created(created_at),
        and when it was updated(updated_at) attributes.
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        """
        converts the BaseModel instance to string representation.
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
