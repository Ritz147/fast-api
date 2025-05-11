from fastapi import APIRouter,status,HTTPException
from typing import List
from fastapi import Depends, Response
import schemas
import models
import database
import repository
import oauth2
from oauth2 import get_current_user
from repository import blog
from sqlalchemy.orm import Session
router=APIRouter(prefix="/blog",tags=["blogs"])
@router.get('',response_model=List[schemas.ShowBlog])
def all(response: Response,db:Session=Depends(database.get_db),current_user:schemas.User=Depends(get_current_user)):
    return blog.get_all(db)
@router.post('', status_code=status.HTTP_201_CREATED)
def create(request:schemas.Blog , db:Session=Depends(database.get_db),current_user:schemas.User=Depends(get_current_user) ):
    return blog.create(db,request)
@router.get('/{id}', status_code=200, response_model=schemas.ShowBlog)
def show(id , response: Response, db: Session = Depends(database.get_db),current_user:schemas.User=Depends(get_current_user)):
    return blog.show(id,db)
@router.delete('/{id}',status_code=status.HTTP_204_NO_CONTENT)
def destroy(id,db:Session=Depends(database.get_db),current_user:schemas.User=Depends(get_current_user)):
    return blog.destroy(id,db)
@router.put('/{id}',status_code=202)
def update(id,request:schemas.Blog,db:Session=Depends(database.get_db),current_user:schemas.User=Depends(get_current_user)):
    return blog.update(id,request,db)