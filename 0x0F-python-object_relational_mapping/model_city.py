#!/usr/bin/python3
"""python file that contains the class definition of a State
and an instance Base = declarative_base()"""

from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import State
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """
    City Class

    Attributes:
        __tablename__ : Table name
        id: state id
        name: state name
    """
    __tablename__ = "cities"
    id = Column(Integer, autoincrement="auto",
                unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("state.id"), nullable=False)
