#!/usr/bin/python3
"""script creates the State 'cali' with the City
'san fran' from the db 'hbtn_0e_100_usa'"""

from sys import argv
from relationship_state import Base, State
from relationship_city import City

from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(*argv[1:]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    session.add(State(name="California",
                      cities=[City(name='San Francisco')]))

    session.close()
