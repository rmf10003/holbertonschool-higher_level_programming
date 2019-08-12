#!/usr/bin/python3
"""script lists all State and corresponding City objects contained in the db"""

from sys import argv
from relationship_state import State
from relationship_city import Base, City

from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(*argv[1:]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    query = session.query(State).order_by(State.id)

    for s in query:
        print("{}: {}".format(s.id, s.name))
        for c in s.cities:
            print("\t{}: {}".format(c.id, c.name))

    session.close()
