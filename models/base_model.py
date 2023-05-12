#!/usr/bin/python3
""" Contains the implementation of the base model """
import uuid
from datetime import datetime
import models


class BaseModel:
    """ the base model that other models inherit from """

    def __init__(self, *args, **kwargs):
        """ initialize a model """

        if kwargs != {}:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                self.__dict__[key] = value
            self.created_at = datetime.strptime(
                self.created_at, '%Y-%m-%dT%H:%M:%S.%f')
            self.updated_at = datetime.strptime(
                self.updated_at, '%Y-%m-%dT%H:%M:%S.%f')
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """ print a representation of the model object """
        return (f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        """ saves the model object, updates the 'updated_at' attribute """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ converts the model object to a dict """
        the_dict = self.__dict__
        the_dict['__class__'] = self.__class__.__name__
        the_dict['created_at'] = self.created_at.isoformat()
        the_dict['updated_at'] = self.updated_at.isoformat()

        return (the_dict)
