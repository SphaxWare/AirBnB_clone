#!/usr/bin/python3
"""BaseModel for AirBnb Clone"""
import uuid
from datetime import datetime as time


class BaseModel:
    """BaseModel Class"""
    def __init__(self):
        """initiate the class"""
        self.id = str(uuid.uuid4())
        self.created_at = time.now()
        self.updated_at = self.created_at

    def __str__(self):
        """string representation of BaseModel"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        updates the public instance attribute 
        updated_at with the current datetime
        """
        self.updated_at = time.now()

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
