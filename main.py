from typing import Optional
from uuid import UUID
from fastapi import FastAPI, HTTPException, Depends # type: ignore
from pydantic import BaseModel
import uvicorn
import models
from database import engine, SessionLocal
from sqlalchemy.orm import Session


app = FastAPI()

models.Base.metadata.create_all(bind=engine)

def get_db():
    try:
        db=SessionLocal()
        yield db
    finally:
        db.close()

class Book(BaseModel):
    title: str
    author: str
    description: str

BOOKS= []

@app.get("/home")
def home_page():
    return "This is home page!!"

#TO DISPLAY THE BOOK DATA IF PRESENT
@app.get("/")
def read_api(db: Session= Depends(get_db)):
    return db.query(models.Books).all()


#TO STORE THE BOOK DATA
@app.post("/")
def create_book(book: Book, db: Session = Depends(get_db)):
    book_model =models.Books(
    title=book.title,
    author=book.author,
    description=book.description
    )

    db.add(book_model)
    db.commit()
    db.refresh(book_model)

    return book


#TO UPDATE THE DETAILS
@app.put("/{book_id}")
def update_book(book_id: int, book: Book, db: Session = Depends(get_db)):
    book_model = db.query(models.Books).filter(models.Books.id == book_id).first()
    
    if book_model is None:
        raise HTTPException(
            status_code=404,
            detail=f"ID {book_id} : Does not exist"
        )
    
    book_model.title = str(book.title)
    book_model.author=str(book.author)
    book_model.description=str(book.description)
    
    db.add(book_model)
    db.commit()
    db.refresh(book_model)

    return book_model

#TO DELETE BOOK DATA
@app.delete("/{book_id}")
def delete_book(book_id: int, db: Session = Depends(get_db)):
    book_model = db.query(models.Books).filter(models.Books.id == book_id).first()
    
    if book_model is None:
        raise HTTPException(
            status_code=404,
            detail=f"ID {book_id} : Does not exist"
        )
    db.query(models.Books).filter(models.Books.id == book_id).delete()

    db.commit()