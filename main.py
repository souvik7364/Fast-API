from routers import product, user, authentication
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from db import engine
import database_models

app = FastAPI() 

@app.get("/")
def root():
    return{"Fatapi server is running"}

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"]
)

database_models.Base.metadata.create_all(bind=engine)

app.include_router(authentication.router)
app.include_router(product.router)
app.include_router(user.router)

