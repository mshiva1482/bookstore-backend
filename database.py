from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Connect to mysql through URL & Create 'bookstore' database in your database
URL_DATABASE = "mysql+pymysql://root:sanjay!14@localhost:3306/bookstore"

engine = create_engine(URL_DATABASE)

session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()