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
    detail = Column(String, index=True)
    recap = Column(String, index=True)
    category = Column(String, index=True)


class Student(Base):
    __tablename__ = 'student'
    
    id = Column(Integer, primary_key=True, index=True)
    fname = Column(String, index=True)
    lname = Column(String, index=True)
    bod = Column(String, index=True)
    sex = Column(String, index=True)
    age = Column(Integer, index=True)

class Menu(Base):
    __tablename__ = 'menu'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    amount = Column(Integer, index=True)
    descript = Column(String, index=True)
    price = Column(Integer, index=True)
    detail = Column(String, index=True)

class Order(Base):
    __tablename__ = 'order'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    amount = Column(Integer, index=True)
    descript = Column(String, index=True)
    price = Column(Integer, index=True)
    

