#!/usr/bin/python3
"""State Model module.
Describes the State class that inherits from BaseModel.
"""
from models.base_model import BaseModel


class State(BaseModel):
    """This class defines the State.
    Attributes:
        name (str): the state's name.
    """

    name = ""
