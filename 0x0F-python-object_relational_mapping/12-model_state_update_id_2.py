#!/usr/bin/python3
"""change the name of a state object from the db"""

from sys import argv
from model_state import Base, State

from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(*argv[1:]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    query = session.query(State).filter(State.id == 2).first()
    query.name = 'New Mexico'

    session.commit()
    session.close()
