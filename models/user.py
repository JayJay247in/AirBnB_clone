#!/usr/bin/python3
"""User Model Module"""

from models.base_model import BaseModel


class User(BaseModel):
    """User class defined from BaseModel"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""