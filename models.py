from sqlalchemy import Column, Integer, String
from database import Base

#Creating Table with table name: books_database
#with following Columns: id, title, author, description
class Books(Base):
    __tablename__= "books"

    id = Column(Integer, primary_key=True, index=True)
    title=Column(String)
    author=Column(String)
    description=Column(String)