#!/usr/bin/python3
# lists all State objects from the database hbtn_0e_6_usa
if __name__ == "__main__":
    import sys
    import sqlalchemy
    from sqlalchemy import create_engine
    from model_state import Base, State
    from sqlalchemy.orm import sessionmaker
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                           (sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for state in session.query(State).filter_by(id='1'):
        print("{}: {}".format(state.id, state.name))
    session.close()
