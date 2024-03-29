#!/usr/bin/python3
"""Script to create the State “California” with the City “San Francisco”
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker
from relationship_city import City
from relationship_state import Base, State

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(username, password, db_name),
                           pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    state = State(name="California")
    city = City(name="San Francisco")
    city.state = state
    session.add(state)
    session.add(city)
    session.commit()
    session.close()
