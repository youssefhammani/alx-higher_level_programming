#!/usr/bin/python3
"""Script to print all City objects from the database hbtn_0e_14_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_city import City
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
        cities = session.query(City, State)\
                .filter(City.state_id == State.id)\
                .order_by(City.id).all()

        for city, state in cities:
            print("{}: ({}) {}".format(state.name, city.id, city.name))
