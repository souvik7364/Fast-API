import models
import database_models
import db
import security
from sqlalchemy.orm import Session
from fastapi import  HTTPException, status

def create(product: models.User, db: Session):
    db_user = database_models.Users(username=product.username, email=product.email, password=security.Hash.hash_password(product.password))
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def show(id: int, db: Session):
    db_user=db.query(database_models.Users).filter(database_models.Users.id == id).first()
    if db_user:
        return db_user    
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with the id {id} is not available")