#!/usr/bin/python3
"""
List all State objects that contain
the letter a from the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(username, password, db_name),
                           pool_pre_ping=True)

    Base.metadata.create_all(engine)

    with Session(engine) as session:
        states_with_a = session.query(State)\
                .filter(State.name.like('%a%'))\
                .order_by(State.id).all()

        for state in states_with_a:
            print("{}: {}".format(state.id, state.name))
