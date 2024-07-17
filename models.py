from sqlalchemy import Boolean, Column, ForeignKey, Integer, String,CHAR
# from sqlalchemy.orm import relationship

from database import Base

class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    author = Column(String, index=True)
    year = Column(Integer, index=True)
    is_published = Column(Boolean, index=True)

class Student(Base):
    __tablename__ = 'student'
    
    id = Column(Integer, primary_key=True, index=True)
    fname = Column(String, index=True)
    lname = Column(String, index=True)
    bod = Column(String, index=True)
    sex = Column(String, index=True)
    age = Column(Integer, index=True)

