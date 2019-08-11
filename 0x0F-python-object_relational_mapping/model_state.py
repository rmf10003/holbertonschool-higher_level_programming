#!/usr/bin/python3
''' module for state class'''

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declaritive_base

Base = declarative_base()

class State(Base):
    """state class"""

    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
