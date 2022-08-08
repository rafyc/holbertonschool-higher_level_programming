#!/usr/bin/env python3
"""Start link class to table in database
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sys import argv
from model_state import Base, State

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1],
        argv[2],
        argv[3],
        pool_pre_ping=True
        ))
    session = Session(engine)
    Base.metadata.create_all(engine)

    new_state1 = State(name='Louisiana')
    session.add(new_state1)
    session.commit()
    session.close()
