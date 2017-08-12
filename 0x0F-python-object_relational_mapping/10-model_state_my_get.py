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

    query = session.query(State.id).filter(State.name == sys.argv[4])
    if query.first() is not None:
        print("{}".format(State.id))
    session.close()
