#!/usr/bin/python3
"""City model module"""

from models.base_model import BaseModel


class City(BaseModel):
    """City class inherited from BaseModel"""
    state_id = ""
    name = ""