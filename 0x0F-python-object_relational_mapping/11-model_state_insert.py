#!/usr/bin/python3
"""
script that adds the State  to the database hbtn_0e_6_usaLouisianaobject
"""

import sys
from model_state import Base, State
from sqlalchemy.orm import Session

from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = Session(engine)
    state = State(name='Louisiana')

    Session.add(state)
    Session.commit()
    print(state.id)

    Session.close()
