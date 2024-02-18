#!/usr/bin/python3
"""python file that contains the class definition of a State
and an instance Base = declarative_base()"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):
    """
    State Class

    Attributes:
        __tablename__ : Table name
        id: state id
        name: state name
    """
    __tablename__ = "states"
    id = Column(Integer, autoincrement="auto",
                unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", back_ref="state",
                          cascade="all, delete-orphan")
