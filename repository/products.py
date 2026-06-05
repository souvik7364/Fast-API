from sqlalchemy.orm import Session
from fastapi import HTTPException, status
import db
import models
import database_models

def get_all(db: Session):
    db_products = db.query(database_models.Product).all()
    return db_products

def show(id: int, db: Session):
    db_product = db.query(database_models.Product).filter(database_models.Product.id == id).first()
    if db_product:
        return db_product    
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Product with the id {id} is not available")
    
def create(product: models.ShowProduct, db: Session, current_user):
    new_product = database_models.Product(
        name=product.name,
        description=product.description,
        price= product.price,
        quantity=product.quantity,
        user_id=current_user.id
    )
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product

def update(id: int, product: models.ShowProduct, db: Session):
    db_product = db.query(database_models.Product).filter(database_models.Product.id == id).first()
    if db_product:
        db_product.name = product.name
        db_product.description = product.description
        db_product.price = product.price
        db_product.quantity = product.quantity
        db.commit()
        return "Product updated"
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Product with id {id} not found")
    
def destroy(id: int, db: Session):
    db_product = db.query(database_models.Product).filter(database_models.Product.id == id).first()
    if db_product:
        db.delete(db_product)
        db.commit()
        return "Product deleted"
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Product with id {id} not found")
