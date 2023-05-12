#!/usr/bin/python3
""" file storage module """
import json
from models.base_model import BaseModel


class FileStorage:
    """ file storage
    __file_path(str): path to database engine
    __objects(dict): dict with key:value pairs where
        key: is the <classname>.<id> of the object
        value: is an obj object
    """

    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        """ nothing to do here """
        pass

    def all(self):
        """ returns the dictonary '__objects' """
        return FileStorage.__objects

    def new(self, obj):
        """ adds a new object to '__objects' """
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """ save to file """
        serialized = {
            key: value.to_dict()
            for key, value in self.__objects.items()
            }
        with open(FileStorage.__file_path, "w") as f:
            json.dump(serialized, f)

    def reload(self):
        """ load from file """
        try:
            with open(FileStorage.__file_path, "r") as f:
                deserialized = json.load(f)
                FileStorage.__objects = {
                    key: eval(value["__class__"])(**value)
                    for key, value in deserialized.items()
                }
        except FileNotFoundError:
            pass
