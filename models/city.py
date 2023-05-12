#!/usr/bin/python3
""" module for class city """
from models.base_model import BaseModel


class City(BaseModel):
    """ City object implementation """
    state_id: str = ""
    name: str = ""