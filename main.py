from typing import Optional
from fastapi import FastAPI, HTTPException, status
from dao import BookDAO
from schemas import Book

app = FastAPI()

@app.get('/')
def home():
    return ('Home')

    
@app.get('/getbook', status_code=status.HTTP_200_OK)
def get_book(id_book:int):
    try:
        item = BookDAO.get(id_book)
        return {"Book": item}
    except Exception as error:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error.args)
    
@app.post('/createbook',status_code=status.HTTP_201_CREATED)
def create_book(book:Book):
    try:
        BookDAO.create(book)
        return book
    except Exception as error:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=error.args)

@app.delete('/deletebook',status_code=status.HTTP_200_OK)
def delete_book(id_book:int):
    try:
        book_exist = BookDAO.get(id_book)
        if(book_exist):
            BookDAO.delete(id_book)
            return {"message": "The book is deleted"}
        raise Exception('Book not found')
    except:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)

@app.get('/listallbooks',status_code=status.HTTP_200_OK)
def list_all_books():
    try:
        books = BookDAO.list()
        return books
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

@app.put('/updatebook',status_code=status.HTTP_200_OK)
def update_book(id_book:int,name:str,isbn:str,quantity:int):
    try:
        book_exist = BookDAO.get(id_book)
        if(book_exist): 
            BookDAO.update(id_book,name,isbn,quantity)
            book_updated = BookDAO.get(id_book)
            return {"Book before": book_exist,"Book updated":book_updated}
    except:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)


         
    

    


