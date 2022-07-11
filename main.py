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
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=error.args)
    
@app.post('/createbook',status_code=status.HTTP_201_CREATED)
def create_book(book:Book):
    try:
        BookDAO.create(book)
        return book
    except Exception as error:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=error.args)
        


    


