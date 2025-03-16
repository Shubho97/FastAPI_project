from typing import Optional
from uuid import UUID
from fastapi import FastAPI # type: ignore
from pydantic import BaseModel
import uvicorn

app = FastAPI()

@app.get("/about")
def about():
    return {"data": {"name": "Shubho"}}
class Book(BaseModel):
    id: UUID
    title: str
    author: str
    description: str

BOOKS= []


