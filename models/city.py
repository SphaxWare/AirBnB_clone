#!/usr/bin/python3
"""
This is the City model
"""
from models.base_model import BaseModel


class City(BaseModel):
    """City class that inherits from BaseModel."""
    state_id: str = ""
    name = ""
