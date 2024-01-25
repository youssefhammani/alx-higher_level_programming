#!/usr/bin/python3
"""Define the State class and instance Base for hbtn_0e_6_usa
"""

from sqlalchemy import Column, Integer, String, Sequence
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """Class representing the 'states' table.
    """
    __tablename__ = 'states'

    id = Column(
        Integer,
        Sequence('state_id_seq'),
        primary_key=True,
        nullable=False
    )
    name = Column(String(128), nullable=False)
