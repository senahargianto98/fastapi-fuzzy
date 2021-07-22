from typing import List
from fastapi import APIRouter, Depends, status, HTTPException
from blog import schemas, database, models, oauth2
from sqlalchemy.orm import Session
from blog.repository import fuzzy

router = APIRouter(
    prefix="/fuzzy",
    tags=['Fuzzy']
)

get_db = database.get_db

 
@router.get('/')
def all(db: Session = Depends(get_db)):
    return fuzzy.get_all(db)

@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request: schemas.Fuzzy, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return fuzzy.create(request, db)