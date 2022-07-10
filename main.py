from fastapi import FastAPI

from dao import BookDAO

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
    
    
    


