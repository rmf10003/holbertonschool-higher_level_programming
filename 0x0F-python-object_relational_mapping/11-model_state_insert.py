#!/usr/bin/python3
"""script to add State object to db"""

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

    LA = State(name='Louisiana')
    session.add(LA)
    session.commit()
    print(LA.id)

    session.close()
