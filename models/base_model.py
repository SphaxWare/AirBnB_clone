#!/usr/bin/python3
"""
BaseModel that provides a foundational
class for representing and managing
common attributes and methods shared
among different entities in the AirBnb Clone.
"""
import models
from uuid import uuid4
from datetime import datetime as time


class BaseModel:
    """
    BaseModel Class that defines all common
    attributes/methods for other classes
    """


    def __init__(self, *args, **kwargs):
        """
        initiate the class
        """
        self.id = str(uuid4())
        self.created_at = time.now()
        self.updated_at = time.now()
        if kwargs:
            for k, v in kwargs.items():
                if k in ['created_at', 'updated_at']:
                    v = time.fromisoformat(v)
        else:
            models.storage.new(self)

    def __str__(self):
        """string representation of BaseModel"""
        return "[{}] ({}) {}".format(
            self.__class__.__name__,
            self.id,
            self.__dict__)

    def save(self):
        """
        updates the public instance attribute
        updated_at with the current datetime
        """
        self.updated_at = time.now()
        models.storage.save()

    def to_dict(self):
        """
        returns a dictionary containing all
        keys/values of __dict__ of the instance
        """
        obj = self.__dict__.copy()
        obj['created_at'] = self.created_at.isoformat()
        obj['updated_at'] = self.updated_at.isoformat()
        obj['__class__'] = self.__class__.__name__
        return obj
