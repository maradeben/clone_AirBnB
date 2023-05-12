#!/usr/bin/python3
""" file storage module """
import json
from models.base_model import BaseModel
from models.user import User
from datetime import datetime


class FileStorage:
    """ file storage
    __file_path(str): path to database engine
    __objects(dict): dict with key:value pairs where
        key: is the <classname>.<id> of the object
        value: is an obj object
    """

    __file_path = "file.json"
    __objects = {}
    valid_models = ['BaseModel']

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

    @property
    def objects(self):
        """ getter method for objects """
        return (self.__objects)

    @objects.setter
    def objects(self, key, attribute, value):
        """ setter method for objects """
        self.__objects[key][attribute] = value
        self.__objects[key]['updated_at'] = datetime.utcnow()

    @staticmethod
    def get_model_n_ids(class_name, id_string):
        """ get ids of all models
    
        Args:
            class_name(str): name of class passed from console
            id_string(str): id of object passed from console

        Return:
            tuple containing:
                list of lists containing [class_names, ids],
                model object if found
        """

        id_class = []
        the_object = ""
        objects = FileStorage.__objects

        # reconstruct key from paased in class and id
        # then try to find it in the objects dict
        key = f"{class_name}.{id_string}"
        try:
            the_object = objects[key]
        except KeyError:
            pass
        for key in objects:
            id_class.append(key.split('.'))
        return (id_class, the_object)

    def delete_model(self, key):
        """ delete model with the given key """

        del FileStorage.__objects[key]

        self.save()

    def print_all(self, class_name=None):
        """ print all available objects thus
            if no class_name is passed, print all objects,
            if class name is passed, print all instances of that class
        
        Args:
            self(BaseModel): BaseModel object
            class_name(str): name of class to see instances of = None
        """

        objects_list = []
        if class_name:
            for key, value in self.__objects.items():
                if class_name == key.split('.')[0]:
                    objects_list.append(f"{key} {value}")
        else:
            for key, value in self.__objects.items():
                objects_list.append(f"{key} {value}")
        
        print(objects_list)

    def update_model(self, *args):
        """ update a model """

        # unpack arguments
        class_name, id_no, attribute, value = args[:4]

        key = f"{class_name}.{id_no}"
        # self.objects(key, attribute, value)
        self.__objects[key].__dict__[attribute] = value
        self.__objects[key].updated_at = datetime.utcnow()
        self.save()
        self.reload()
