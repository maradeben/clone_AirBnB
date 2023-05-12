#!/usr/bin/python3
""" module for class amenity """
from models.base_model import BaseModel


class Amenity(BaseModel):
    """ Amenity object implementation """
    name: str = ""