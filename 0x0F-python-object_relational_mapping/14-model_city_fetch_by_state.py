#!/usr/bin/python3
"""
a script 14-model_city_fetch_by_state.py that prints all City objects from
the database hbtn_0e_14_usa
"""
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password,
                                   dbname), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    res = session.query(City.name, City.id, State.name).join(State).all()
    for city in res:
        print("{}: ({}) {}".format(city[2], city[1], city[0]))
    session.close()
