from typing import Optional
from uuid import UUID
from fastapi import FastAPI, HTTPException # type: ignore
from pydantic import BaseModel
import uvicorn


app = FastAPI()

class Book(BaseModel):
    id: UUID
    title: str
    author: str
    description: str

BOOKS= []

@app.get("/home")
def home_page():
    return "This is home page!!"

#TO DISPLAY THE BOOK DATA IF PRESENT
@app.get("/")
def about():
    return BOOKS

#TO STORE THE BOOK DATA
@app.post("/")
def create_book(book: Book):
    BOOKS.append(book)
    return book


#TO UPDATE THE DETAILS
@app.put("/{book_id}")
def update_book(book_id: UUID, book: Book):
    counter= 0

    for x in BOOKS:
        counter +=1
        if x.id== book_id:
            BOOKS[counter - 1] = book
            return BOOKS[counter-1]
    
    raise HTTPException(
        status_code=404,
        detail=f"ID {book_id} : Does not exist"
    )

#TO DELETE BOOK DATA
@app.delete("/{book_id}")
def delete_book(book_id: UUID, book: Book):
    counter= 0

    for x in BOOKS:
        counter +=1
        if x.id== book_id:
            del BOOKS[counter - 1]
            return f"ID: {book_id} is deleted"
    
    raise HTTPException(
        status_code=404,
        detail=f"ID {book_id} : Does not exist"
    )