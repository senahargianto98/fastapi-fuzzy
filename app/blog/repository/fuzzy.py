from typing import List
from sqlalchemy.orm import Session
from blog import models, schemas
from fastapi import HTTPException, status
from fuzzywuzzy import process
import re


def get_all(db: Session):
    model = models.Fuzzy.query
    model1 = models.Fuzzy.result  
    blogs = db.query(model).all()
    blogs1 = db.query(model1).all()
    blogs2 = blogs
    test = (
        re.sub('\d', '',format(process.extractOne(str(bean)
        .replace(',','')
        .replace('(', '')
        .replace(')', '')
        .replace("'", '')
        .replace("'", ''),
        ["sena, adalah bla bla bla bla","febrisena, adalah blablablabla"])))
        .replace('(', '').replace(')', '')
        .replace("'", '').replace("'", '')
        for bean in blogs2
    )
    test1 = blogs1
    return test,test1

def create(request: schemas.Fuzzy, db: Session):
    model = models.Fuzzy(
        query=request.query, 
        result= request.result
    )
    db.add(model)
    db.commit()
    db.refresh(model)
    return model