#!/usr/bin/python3
"""script that deletes all State objects containing
letter 'a' from db hbtn_0e_6_usa"""

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

    query = session.query(State).filter(State.name.like('%a%'))

    for instance in query:
        session.delete(instance)

    session.commit()
    session.close()
