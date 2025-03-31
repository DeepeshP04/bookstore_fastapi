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
DATABASE_URL = "postgresql://{POSTGRES_USER}:{POSTGRES_PASS}@localhost:5432/bookstore"