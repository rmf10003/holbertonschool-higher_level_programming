#!/usr/bin/python3
"""script that lists all State objects containing
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

    query = session.query(State).filter(State.name.
                                        like('%a%')).order_by(State.id.asc())

    for instance in query:
        print("{}: {}".format(instance.id, instance.name))

    session.close()
