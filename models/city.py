#!/usr/bin/python3
"""City Model module.
Defines the City class that inherits from BaseModel.
"""
from models.base_model import BaseModel


class City(BaseModel):
    """The class defines a City.
    Attributes:
        state_id (str): the city's state id.
        name (str): the city's name.
    """

    state_id = ""
    name = ""
