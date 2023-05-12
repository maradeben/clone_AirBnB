#!/usr/bin/python3
""" module for class review """
from models.base_model import BaseModel


class Review(BaseModel):
    """ Review object implementation """
    place_id: str = ""
    user_id: str = ""
    text: str = ""
