#!/usr/bin/python3
"""Storage Module"""
import json
import os


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
        """deserializes the JSON file to __objects"""
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as f:
                data = json.load(f)
                for key, serialized_data in data.items():
                    cls_name, cls_id = key.split('.')
                    cls = globals()[cls_name]
                    instance = cls(**serialized_data)
                    self.__objects[key] = instance
