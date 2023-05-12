#!/usr/bin/python3
""" user object module """
from models.base_model import BaseModel



class User(BaseModel):
    """ user class that inherits from BaseModel """

    email: str = ""
    password: str = ""
    first_name: str = ""
    last_name: str = ""
