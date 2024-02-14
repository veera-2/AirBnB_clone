#!/usr/bin/python3
"""Amenity Model module.
Defines the Amenity class that inherits from BaseModel.
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """The class defines an Amenity.
    Attributes:
        name (str): Amenity's name.
    """

    name = ""
