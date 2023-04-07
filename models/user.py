#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import os
import hashlib


class User(BaseModel, Base):
    """This class defines a user by various attributes"""

    # check storage
    # storage = os.getenv('HBNB_TYPE_STORAGE')
    # if storage == 'db':

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = 'users'
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
        places = relationship("Place", backref="user", cascade="all, delete")
        reviews = relationship("Review", backref="user", cascade="all, delete")
    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""

    def __init__(self, *args, **kwargs):
        """initializes user"""
        super().__init__(*args, **kwargs)
        if self.password:
            self.password = self.hash_password(self.password)

    def hash_password(self, password):
        hash_object = hashlib.md5()
        hash_object.update(password.encode('utf-8'))
        return hash_object.hexdigest()
