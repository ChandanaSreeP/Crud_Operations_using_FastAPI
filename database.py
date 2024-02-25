# Importing necessary modules from SQLAlchemy
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine

# Creating a SQLAlchemy engine to connect to the PostgreSQL database
# Replace 'postgresql://postgres:pcs123@localhost/Person' with your actual database URL
# 'echo=True' enables logging of all SQL statements
engine = create_engine('postgresql://postgres:pcs123@localhost/Person', echo=True)

# Creating a base class for declarative class definitions
Base = declarative_base()

# Creating a session maker to generate database sessions bound to the engine
SessionLocal = sessionmaker(bind=engine)

# Note: This file sets up the SQLAlchemy engine, base class, and session maker
# for connecting to a PostgreSQL database named 'Person'.
# Make sure to replace the database URL with your actual database URL.
# The 'echo=True' parameter enables logging of all SQL statements, which can be helpful for debugging.
