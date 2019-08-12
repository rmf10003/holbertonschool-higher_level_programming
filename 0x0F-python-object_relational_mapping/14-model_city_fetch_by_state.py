#!/usr/bin/python3
"""script that lists all city objects from db hbtn_0e_14_usa"""

from sys import argv
from model_state import Base, State
from model_city import City

from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    query = session.query(City, State).\
        filter(State.id == City.state_id).order_by(City.id)
    for city, state in query:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.close()
