#!/usr/bin/python3
"""
This is the Review model
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Review class that inherits from BaseModel."""
    place_id: str = ""
    user_id: str = ""
    text: str = ""
