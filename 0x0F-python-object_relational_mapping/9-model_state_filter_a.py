#!/usr/bin/python3
"""
a script that lists all State objects that contain the letter a from
the database hbtn_0e_6_usa
"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password,
                                   dbname), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)
    session = Session()
    query = session.query(State).filter(
        State.name.like('%a%')).order_by(State.id).all()
    for state in query:
        print("{}: {}".format(state.id, state.name))
    session.close()
