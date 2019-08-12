#!/usr/bin/python3
"""script creates the State 'cali' with the City
'san fran' from the db 'hbtn_0e_100_usa'"""

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

    casf = State(name="California",
                 cities=[City(name='San Francisco')])
    session.add(casf)
    session.commit()

    session.close()
