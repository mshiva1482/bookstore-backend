from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel
from typing import Annotated
import auth
from starlette.status import HTTP_200_OK, HTTP_401_UNAUTHORIZED
import models
from database import Base, engine, session_local
from sqlalchemy.orm import Session
from auth import get_current_user

app = FastAPI()
app.include_router(auth.router)

models.Base.metadata.create_all(bind=engine)


class post_book(BaseModel):
    # input validation
    isbn: int
    title: str
    author: str
    price: float
    quantity: int


def get_db():
    db = session_local()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]
user_dependency = Annotated[dict, Depends(get_current_user)]

# To create new books and add it to the database - AUTHENTICATION REQUIRED
@app.post("/books/", status_code=status.HTTP_201_CREATED)
async def add_book(user: user_dependency, book: post_book, db: db_dependency):
    if user is None:
        raise HTTPException(
            status_code=HTTP_401_UNAUTHORIZED, detail="Authentication Failed"
        )
    else:
        db_book = models.Book(**book.dict())
        db.add(db_book)
        db.commit()
        return {"message": "Book has been created!"}

# To view a book based on isbn number
@app.get("/book/{isbn}", status_code=status.HTTP_200_OK)
async def get_book(isbn: int, db: db_dependency):
    book = db.query(models.Book).filter(models.Book.isbn == isbn).first()
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

# To view all books
@app.get("/books/", status_code=status.HTTP_200_OK)
async def get_all_books(db: db_dependency):
    book = db.query(models.Book).all()
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

# To update details about a book based on isbn number - AUTHENTICATION REQUIRED
@app.put("/book/{isbn}", status_code=status.HTTP_200_OK)
async def update_book(
    isbn: int, updated_book: post_book, user: user_dependency, db: db_dependency
):
    if user is None:
        raise HTTPException(
            status_code=HTTP_401_UNAUTHORIZED, detail="Authentication Failed"
        )
    else:
        existing_book = db.query(models.Book).filter(models.Book.isbn == isbn).first()
        if existing_book is None:
            raise HTTPException(status_code=404, detail="Book not found")
        for key, value in updated_book.dict().items():
            setattr(existing_book, key, value)
        db.commit()
        return {"message": "Book has been updated!"}

# To delete a book - AUTHENTICATION REQUIRED
@app.delete("/book/{isbn}", status_code=HTTP_200_OK)
async def delete_book(isbn: int, user: user_dependency, db: db_dependency):
    if user is None:
        raise HTTPException(
            status_code=HTTP_401_UNAUTHORIZED, detail="Authentication Failed"
        )
    else:
        db_book = db.query(models.Book).filter(models.Book.isbn == isbn).first()
        if db_book is None:
            raise HTTPException(status_code=404, detail="Book not found")
        db.delete(db_book)
        db.commit()
        return {"message": "Book Deleted!"}
