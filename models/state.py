#!/usr/bin/python3
""" module for class state """
from models.base_model import BaseModel


class State(BaseModel):
    """ State object implementation """
    name: str = ""