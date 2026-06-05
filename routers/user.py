from fastapi import APIRouter, Depends
import models
import db
from sqlalchemy.orm import Session
from repository import users

router=APIRouter(
    prefix="/user",
    tags=['Users']
)

@router.post('/', response_model=models.ShowUser)
def create_user(product: models.User, db: Session = Depends(db.get_db)):
    return users.create(product, db)

@router.get('/{id}', response_model=models.ShowUser)
def get_user_by_id(id:int, db: Session = Depends(db.get_db)):
    return users.show(id, db)
