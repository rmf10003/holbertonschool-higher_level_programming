#!/usr/bin/python3
"""script lists all City objects from db"""

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

    query = session.query(City).order_by(City.id)

    for c in query:
        print("{}: {} -> {}".format(c.id, c.name, c.state.name))

    session.close()
