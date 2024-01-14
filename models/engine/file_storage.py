#!/usr/bin/python3
"""Storage Module"""
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State


class FileStorage:
    """
    Class that serializes instances to a JSON file and
    deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        serialized_objs = {}
        for k, v in self.__objects.items():
            serialized_objs[k] = v.to_dict()

        with open(self.__file_path, "w") as f:
            json.dump(serialized_objs, f)

    def reload(self):
        """
        Deserializes the JSON file to __objects
        """

        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as f:
                data = json.load(f)
                for k, v in data.items():
                    # get the class name and id
                    cls_name, obj_id = k.split('.')
                    # create an instance from the json data
                    cls_instance = globals()[cls_name](**v)
                    # Add the instance back to __objects
                    self.new(cls_instance)
