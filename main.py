#Python
from typing import Optional

#Pydantic
from pydantic import BaseModel

# FastAPI
from fastapi import FastAPI
from fastapi import Body, Query, Path

app = FastAPI()

#Modedl


class Location(BaseModel):
    city: str
    stete: str
    country: str

class Person(BaseModel):
    first_name: str
    last_name: str
    age: int
    hair_calor: Optional[str] = None
    is_married: Optional[bool] = None
       

@app.get("/")
def home():
    return {"hello": "world"}


#reguest and response Body

@app.post("/person/new")
def creat_person(person: Person = Body(...)):
    return person

#validacion: Query Parameters

@app.get("/person/detail")
def show_person(
    name: Optional[str] = Query(
        None, 
        min_length=1, 
        max_length=50,
        title="person_name",
        description="this is the person name. It's between 1 and 50 characters"
        ),
    age: str =Query(
        ...,
        title="Person Age",
        description="this is the person age. It's required"
        )
):
    return {name: age}

# validaciones: Path Parameters
@app.get("/person/datail/{person_id}")
def show_person(
    person_id: int = Path(
        ..., 
        gt=0
        ),
        
):
    return {person_id: "It exists"}

# VAlidaciones en request Body

@app.put("person/{person_id}")
def update_person(
    person_id: int = Path(
        ...,
        title="Person ID",
        description="This is the person ID",
        gt=0
    ),
    person:Person = Body(...,),
    location : Location = Body(...)
):
    results = person.dict()
    results.update(location.dict())
    return results
    