from fastapi import FastAPI, Depends, HTTPException
import services, models, schemas
from database import get_db, engine
from sqlalchemy.orm import Session

app = FastAPI()

@app.get("/books/", response_model=list[schemas.Book])
def get_all_books(db: Session = Depends(get_db)):
    return services.get_books(db)

@app.get("/books/{book_id}", response_model=schemas.Book)
def get_book_by_id(book_id: int, db: Session = Depends(get_db)):
    book_queryset = services.get_book_by_id(db, book_id)
    if book_queryset:
        return book_queryset
    raise HTTPException(status_code=404, detail="Book not found")

@app.post("/books/", response_model=schemas.Book)
def create_new_book(book: schemas.BookCreate, db: Session = Depends(get_db)):
    return services.create_book(db, book)