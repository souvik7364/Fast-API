from typing import List, Annotated
from fastapi import APIRouter, Depends, status, HTTPException
import models
import db
from oauth2 import get_current_user
from sqlalchemy.orm import Session
from repository import products

router = APIRouter(
    prefix="/products",
    tags=['Product']
)

@router.get("/", response_model=List[models.ShowProduct])
def get_all_products(current_user: Annotated[models.User, Depends(get_current_user)], db: Session = Depends(db.get_db)):
    return products.get_all(db)
    
@router.get("/{id}", status_code=200, response_model=models.ShowProduct)
def get_product_by_id(current_user: Annotated[models.User, Depends(get_current_user)], id: int, db: Session = Depends(db.get_db)):
    return products.show(id, db)

@router.post("/", status_code=status.HTTP_201_CREATED,response_model=models.ShowProduct)
def add_product(current_user: Annotated[models.User, Depends(get_current_user)], product: models.ShowProduct, db: Session = Depends(db.get_db)):
    return products.create(product, db, current_user)

@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED)
def update_product(current_user: Annotated[models.User, Depends(get_current_user)], id: int, product: models.ShowProduct, db: Session = Depends(db.get_db)):
    return products.update(id, product, db)

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_product(current_user: Annotated[models.User, Depends(get_current_user)], id: int, db: Session = Depends(db.get_db)):
    return products.destroy(id, db)