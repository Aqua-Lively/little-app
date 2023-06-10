from fastapi import FastAPI
from . import models
from .database import engine
from .routes import post

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(post.router)








@app.get('/')
def root():
    return{'message': 'hello'}
