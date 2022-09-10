#!/usr/bin/python3
"""
Prints all State objects and their City objects
from the database hbtn_0e_101_usa
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from relationship_state import Base, State
from relationship_city import City


if __name__ == '__main__':
    eng = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(argv[1],
                                                                    argv[2],
                                                                    argv[3]))
    Base.metadata.create_all(eng)
    Session = sessionmaker(bind=eng)
    session = Session()
    rows = session.query(State).all()
    for state in rows:
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("    {}: {}".format(city.id, city.name))
    session.close()
