from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

fakeDB = []

class Films(BaseModel):
    id : int
    name : str
    is_hollywood : Optional[bool] = False

#root api
@app.get('/')
def index():
    return {'Messages':'Hello World!'}

#get all film recodes
@app.get('/films')
def all_films():
    return fakeDB

#get specific film
@app.get('/film/{film_id}')
def film_from_id(film_id : int):
    return fakeDB[film_id - 1]

#add a new film
@app.post('/add_film')
def add_film(film:Films):
    fakeDB.append(film.dict())
    print(fakeDB)
    return fakeDB[-1]

#delete a film recode
@app.delete('/remove_film/{film_id}')
def remove_film(film_id:int):
    fakeDB.pop(film_id - 1)
    return {'Message':'Deletion successfull'}
