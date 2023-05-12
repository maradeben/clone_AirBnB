""" Contains the implementation of the base model """
import uuid
import datetime

class BaseModel:
    """ the base model that other models inherit from """

    def __init__(self):
        """ initialize a model """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()
    
    def __str__(self):
        """ print a representation of the model object """
        return (f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")
    
    def save(self):
        """ saves the model object, updates the 'updated_at' attribute """
        self.updated_at = datetime.datetime.now()
    
    def to_dict(self):
        """ converts the model object to a dict """
        the_dict = self.__dict__
        the_dict['__class__'] = self.__class__.__name__
        the_dict['created_at'] = self.created_at.isoformat()
        the_dict['updated_at'] = self.updated_at.isoformat()

        return (the_dict)
