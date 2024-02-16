#!/usr/bin/python3
"""Start link class to table in database
"""
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """get DB data and modify them"""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    cities = session.query(City)
    states = session.query(State)
    for state in states:
        for city in cities:
            if city.state_id == state.id:
                print(f"{state.name}: ({city.id}) {city.name}")
    session.close()
