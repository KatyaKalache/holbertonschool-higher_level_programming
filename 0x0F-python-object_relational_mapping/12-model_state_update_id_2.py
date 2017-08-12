#!/usr/bin/python3
# changes the name of a State
if __name__ == "__main__":
    import sys
    import sqlalchemy
    from sqlalchemy import create_engine
    from model_state import Base, State
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import update

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                           (sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    session.query(State).filter_by(id=2).update({"name": u"New Mexico"})
    session.commit()
    session.close()
