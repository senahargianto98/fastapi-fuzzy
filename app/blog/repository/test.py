from typing import List
from sqlalchemy.orm import Session
from blog import models, schemas
from fastapi import HTTPException, status
 
def get_all(db: Session):
    model = models.Test.a1
    model2 = models.Test.a2
    blogs = db.query(model,model2).all()
    return blogs

def create(request: schemas.Test, db: Session):
    model = models.Test(
        a1=request.a1, 
        a2=request.a2, 
        hasil= request.a1*request.a2)
    db.add(model)
    db.commit()
    db.refresh(model)
    return model