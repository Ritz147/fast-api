from fastapi import FastAPI,Depends,Response,status,HTTPException
import schemas
import hashing
from database import engine,get_db
from typing import List
from routers import blog,user,authentication
app=FastAPI()
import models
models.Base.metadata.create_all(engine)
from sqlalchemy.orm import Session
from passlib.context import CryptContext

app.include_router(blog.router)
app.include_router(user.router)
app.include_router(authentication.router)