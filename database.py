# import necessary libraries
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

import os
from dotenv import load_dotenv

# load all the environment variables from the .env file
load_dotenv()

POSTGRES_USER = os.getenv('POSTGRES_USER')
POSTGRES_PASS = os.getenv('POSTGRES_PASS')

# initialize the database URL
DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASS}@localhost:5432/bookstore"

# create engine for managing the database connection
engine = create_engine(DATABASE_URL)

# create a session local class for managing sessions
# and a base class for all the models or tables
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
# create the database tables
def create_table():
    Base.metadata.create_all(bind=engine)