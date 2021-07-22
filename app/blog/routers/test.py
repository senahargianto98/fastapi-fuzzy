from typing import List
from fastapi import APIRouter, Depends, status, HTTPException
from blog import schemas, database, models, oauth2
from sqlalchemy.orm import Session
from blog.repository import test 

router = APIRouter(
    prefix="/test",
    tags=['Tests']
)

get_db = database.get_db

 
@router.get('/')
def all(db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return test.get_all(db)

@router.post('/', status_code=status.HTTP_201_CREATED,)
def create(request: schemas.Test, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return test.create(request, db)
