from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI, Depends, Response, APIRouter
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

# Import models
from database import SessionLocal, engine
import models

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
router_v1 = APIRouter(prefix='/api/v1')

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# https://fastapi.tiangolo.com/tutorial/sql-databases/#crud-utils

#BOOKS
@router_v1.get('/books')
async def get_books(db: Session = Depends(get_db)):
    return db.query(models.Book).all()

@router_v1.get('/books/{book_id}')
async def get_book(book_id: int, db: Session = Depends(get_db)):
    return db.query(models.Book).filter(models.Book.id == book_id).first()

@router_v1.post('/books')
async def create_book(book: dict, response: Response, db: Session = Depends(get_db)):
    # TODO: Add validation
    newbook = models.Book(title=book['title'], author=book['author'], year=book['year'], is_published=book['is_published'], detail=book['detail'], recap=book['recap'], category=book['category'])
    db.add(newbook)
    db.commit()
    db.refresh(newbook)
    response.status_code = 201
    return newbook

@router_v1.patch('/books/{book_id}')
async def update_book(book_id: int, book: dict, db: Session = Depends(get_db)):
    db_item = db.query(models.Book).filter(models.Book.id == book_id).first()
    for key, value in book.items():
            setattr(db_item, key, value)
    db.commit()
    db.refresh(db_item)
    # response.status_code = 201
    return db_item

@router_v1.delete('/books/{book_id}')
async def delete_book(book_id: int,db: Session = Depends(get_db)):
    db_item = db.query(models.Book).filter(models.Book.id == book_id).first()
    db.delete(db_item)
    db.commit()
    return "Delete"

#STUDENTS
@router_v1.get('/student')
async def get_student(db: Session = Depends(get_db)):
    return db.query(models.Student).all()

@router_v1.get('/student/{student_id}')
async def get_student(student_id: int, db: Session = Depends(get_db)):
    return db.query(models.Student).filter(models.Student.id == student_id).first()

@router_v1.post('/student')
async def create_student(student: dict, response: Response, db: Session = Depends(get_db)):
    # TODO: Add validation
    newstudent = models.Student(id=student['id'], fname=student['fname'], lname=student['lname'], bod=student['bod'], age=student['age'], sex=student['sex'])
    db.add(newstudent)
    db.commit()
    db.refresh(newstudent)
    response.status_code = 201
    return newstudent

#MENUS
@router_v1.get('/menu')
async def get_menu(db: Session = Depends(get_db)):
    return db.query(models.Menu).all()

@router_v1.get('/menu/{menu_id}')
async def get_menu(menu_id: int, db: Session = Depends(get_db)):
    return db.query(models.Menu).filter(models.Menu.id == menu_id).first()

@router_v1.post('/menu')
async def create_menu(menu: dict, response: Response, db: Session = Depends(get_db)):
    # TODO: Add validation
    newmenu = models.Menu(name=menu['name'], amount=menu['amount'], descript=menu['descript'], detail=menu['detail'] ,price=menu['price'])
    db.add(newmenu)
    db.commit()
    db.refresh(newmenu)
    response.status_code = 201
    return newmenu

@router_v1.patch('/menu/{menu_id}')
async def update_menu(menu_id: int, menu: dict, db: Session = Depends(get_db)):
    db_item = db.query(models.Menu).filter(models.Menu.id == menu_id).first()
    for key, value in menu.items():
            setattr(db_item, key, value)
    db.commit()
    db.refresh(db_item)
    return db_item

@router_v1.delete('/menu/{menu_id}')
async def delete_menu(menu_id: int, db: Session = Depends(get_db)):
    db_item = db.query(models.Menu).filter(models.Menu.id == menu_id).first()
    db.delete(db_item)
    db.commit()
    return "Delete"

#ORDERS
@router_v1.get('/order')
async def get_order(db: Session = Depends(get_db)):
    return db.query(models.Order).all()

@router_v1.get('/order/{order_id}')
async def get_order(order_id: int, db: Session = Depends(get_db)):
    return db.query(models.Order).filter(models.Order.id == order_id).first()

@router_v1.post('/order')
async def create_order(order: dict, response: Response, db: Session = Depends(get_db)):
    neworder = models.Order(name=order['name'], amount=order['amount'], descript=order['descript'], price=order['price'])
    db.add(neworder)
    db.commit()
    db.refresh(neworder)
    response.status_code = 201
    return neworder

@router_v1.patch('/order/{order_id}')
async def update_order(order_id: int, order: dict, db: Session = Depends(get_db)):
    db_item = db.query(models.Order).filter(models.Order.id == order_id).first()
    for key, value in order.items():
            setattr(db_item, key, value)
    db.commit()
    db.refresh(db_item)
    return db_item

@router_v1.delete('/order/{order_id}')
async def delete_order(order_id: int, db: Session = Depends(get_db)):
    db_item = db.query(models.Order).filter(models.Order.id == order_id).first()
    db.delete(db_item)
    db.commit()
    return "Delete"

app.include_router(router_v1)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app)

