#!/usr/bin/python3
"""
Script that lists all State objects from the database - Using module SQLAlchemy
"""
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(argv) != 4:
        print("Usage: {} username password database".format(argv[0]))
        exit(1)

    # Database connection parameters
    username, password, database = argv[1], argv[2], argv[3]
    connection_string = 'mysql+mysqldb://{}:{}@localhost/{}'.format(
        username, password, database)

    # Create an engine
    engine = create_engine(connection_string, pool_pre_ping=True)

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session
    session = Session()

    # Create database tables if they don't exist
    Base.metadata.create_all(engine)

    try:
        # Query for all State objects and print their details
        states = session.query(State).order_by(State.id).all()
        for state in states:
            print("{}: {}".format(state.id, state.name))
    except Exception as e:
        print("Error:", e)
        session.rollback()  # Rollback changes in case of error
    finally:
        session.close()  # Close the session
