# Import necessary modules
from sqlalchemy import String, Integer, Column, Boolean
from database import Base, engine  # Import database connection and Base class

# Function to create database tables based on defined models
def create_tables():
    # Create all tables defined in Base's metadata
    Base.metadata.create_all(engine)

# Define a SQLAlchemy model for the 'person' table
class Person(Base):
    # Set the table name
    __tablename__ = "person"

    # Define columns for the 'person' table
    id = Column(Integer, primary_key=True)        # Primary key column
    firstname = Column(String(50), nullable=False)  # First name column (String with max length of 50 characters, not nullable)
    lastname = Column(String(50), nullable=False)   # Last name column (String with max length of 50 characters, not nullable)
    isFemale = Column(Boolean)                     # Boolean column to represent gender

# PostgreSQL database driver to connect Python programs to PostgreSQL databases: pip install psycopg2-binary
