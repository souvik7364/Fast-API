from sqlalchemy import Column, Integer, String, Float, ForeignKey
from db import Base
from sqlalchemy.orm import relationship

class Product(Base):

    __tablename__ = "product"

    id = Column(Integer, primary_key = True, index = True)
    name = Column(String(255))
    description = Column(String(500))
    price = Column(Float)
    quantity = Column(Integer)
    user_id = Column(Integer, ForeignKey('users.id'))

    owner = relationship("Users", back_populates="product")

class Users(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key = True, index = True)
    username = Column(String(255))
    email = Column(String(555))
    password = Column(String(1000))

    product = relationship("Product", back_populates="owner")