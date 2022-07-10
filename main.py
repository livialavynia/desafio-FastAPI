from fastapi import FastAPI
from dao import BookDAO
from schemas import Book

app = FastAPI()

@app.get('/')
def home():
    return ('Home')

    
@app.get('/getbook/{id_book}')
def get_book(id_book:int):
    try:
        item = BookDAO.get(id_book)
        return {"Book": item}
    except:
        return {"error":'error'}
    
@app.post('/createbook')
def create_book(book:Book):
    result_create_book = BookDAO.create(book)
    return result_create_book

    


