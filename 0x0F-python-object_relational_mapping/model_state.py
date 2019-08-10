#!/usr/bin/python3
''' module for state class'''

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declaritive_base

Base = declarative_base()

class State(Base):
    """state class"""

    id = Column(Integer, primary_key=True)
    name = Column(String(128))
