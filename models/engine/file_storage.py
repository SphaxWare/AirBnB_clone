#!/usr/bin/python3
"""Storage Module"""
import json
import os


class FileStorage:
    """
    Class that serializes instances to a JSON file and
    deserializes JSON file to instances
    """
    def __init__(self):
        """Constructor for FileStorage"""
        self.__file_path = "file.json"
        self.__objects = []

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        self.__objects[obj.__class__.__name__.id] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        with open(self.__file_path, "w") as f:
            json.dump(self.__objects, f)

    def reload(self):
        """deserializes the JSON file to __objects"""
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as f:
                self.__objects = json.load(f)
