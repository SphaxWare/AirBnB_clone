#!/usr/bin/python3
"""
This is the Amenity model
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity class that inherits from BaseModel."""
    name: str = ""
