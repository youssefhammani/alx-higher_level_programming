#!/usr/bin/python3
"""Print the first State object from the database hbtn_0e_6_usa
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
        first_state = session.query(State).order_by(State.id).first()

        if first_state:
            print("{}: {}".format(first_state.id, first_state.name))
        else:
            print("Nothing")
