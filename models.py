from operator import index
from sqlalchemy import Column, Integer, String, Float
from database import Base


class Book(Base):
    __tablename__ = "books"

    isbn = Column(Integer, primary_key=True, index=True)
    title = Column(String(50), index=True)
    author = Column(String(50), index=True)
    price = Column(Float)
    quantity = Column(Integer)


class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(20), unique=True)
    hashed_password = Column(String(100))
