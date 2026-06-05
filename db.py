
from models import Product
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from config import db_url
engine = create_engine(db_url, pool_pre_ping=True, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


# products = [
#     Product(name="Phone", description="A Smartphone", price=699.99, quantity=50),
#     Product(name="Laptop", description="A Powerful Laptop", price=999.99, quantity=30),
#     Product(name="Pen", description="A blue pen", price=2.99, quantity=200),
# ]

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def init_db():
    import database_models
    db = SessionLocal()
    existing_count = db.query(database_models.Product).count()
    if existing_count == 0:
        # for product in products:
        #     db.add(database_models.Product(**product.model_dump()))
        # db.commit()
        pass
    db.commit()
    db.close()
init_db()
