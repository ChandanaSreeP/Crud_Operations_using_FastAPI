# Importing necessary modules and classes from FastAPI, Pydantic, and the database
from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel
from database import SessionLocal
import models

# Creating a FastAPI instance
app = FastAPI()

# Creating a base model for Pydantic models with ORM mode enabled
class OurBaseModel(BaseModel):
    class Config:
        orm_mode = True

# Defining the Pydantic model for the Person entity
class Person(OurBaseModel):
    id: int
    firstname: str
    lastname: str
    isFemale: bool

# Creating a database session
db = SessionLocal()

#Endpoint for the home page
@app.get("/",status_code=status.HTTP_200_OK)
def greeting():
    return "Welcome to our app go to /docs for more information"

# Endpoint to get all persons
@app.get('/getallusers', response_model=list[Person], status_code=status.HTTP_200_OK)
def getAllPersons():
    getAllPersons = db.query(models.Person).all()
    return getAllPersons

# Endpoint to get a single person by ID
@app.get('/getbyid/{person_id}', response_model=Person, status_code=status.HTTP_200_OK)
def getSinglePerson(person_id: int):
    getsinglePerson = db.query(models.Person).filter(models.Person.id == person_id).first()
    if getsinglePerson is not None:
        return getsinglePerson
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Person Not Found")

# Endpoint to add a new person
@app.post('/addperson', response_model=Person, status_code=status.HTTP_201_CREATED)
def addPerson(person: Person):
    newPerson = models.Person(
        id=person.id,
        firstname=person.firstname,
        lastname=person.lastname,
        isFemale=person.isFemale
    )
    find_person = db.query(models.Person).filter(models.Person.id == person.id).first()
    if find_person is not None:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail='Person already Exists')
    db.add(newPerson)
    db.commit()
    return newPerson

# Endpoint to update an existing person
@app.put('/update_person/{person_id}', response_model=Person, status_code=status.HTTP_202_ACCEPTED)
def updatePerson(person_id: int, person: Person):
    find_person = db.query(models.Person).filter(models.Person.id == person_id).first()
    if find_person is not None:
        find_person.id = person.id
        find_person.firstname = person.firstname
        find_person.lastname = person.lastname
        find_person.isFemale = person.isFemale
        db.commit()
        return find_person
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Person Not Found")

# Endpoint to delete a person by ID
@app.delete("/deleteperson/{person_id}", response_model=Person, status_code=status.HTTP_200_OK)
def deletePerson(person_id: int):
    find_person = db.query(models.Person).filter(models.Person.id == person_id).first()
    if find_person is not None:
        db.delete(find_person)
        db.commit()
        raise HTTPException(status_code=status.HTTP_200_OK, detail="Person deleted successfully")
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Person is already deleted or Not Found")


''' 
@app.get('/',status_code=200)
def getPerson_Info():
  return {'message' : 'Server is running'}

# Uvicorn s used to run apps
# python -m uvicorn main:app  - to run the code
# python -m uvicorn main:app --reload

# Pydantic is used to for data manipulation and validation
@app.get('/getpersonbyid/{person_id}',status_code=200)
def getPerson_By_Id(person_id: int):
  return {'message': f'Your Person Id is {person_id}'}

@app.post('/addpersoninfo',status_code=200)
def addPerson_Info(person: Person):
  return {
    'id': person.id,
    'firstname': person.firstname,
    'lastname': person.lastname,
    'isFemale': person.isFemale,
  }
'''
# sqlalchemy - used for connecting the database
