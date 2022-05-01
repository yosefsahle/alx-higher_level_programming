#!/usr/bin/python3
"""
script 14-model_city_fetch_by_state.py that prints all City objects
 from the database hbtn_0e_14_usa
"""

import sys
from model_state import Base, State
from model_city import City
from sqlalchemy.orm import Session

from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = Session(engine)
    rows = Session.query(State, City).join(City).all()
    for row in rows:
        print("{}: ({}) {}".format(row[0].name, row[1].id, row[1].name))

    Session.close()
