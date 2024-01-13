#!/usr/bin/python3
"""Module to define the State class
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from relationship_city import Base


class State(Base):
    """State class that inherits from Base
    """

    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)

    cities = relationship(
            "City",
            cascade="all,
            delete",
            back_populates="state"
    )
