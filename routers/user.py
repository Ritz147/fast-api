from fastapi import APIRouter
import schemas , models ,database
from sqlalchemy.orm import Session
from fastapi import Depends, status, HTTPException
from database import get_db
import hashing
from typing import List
from repository import user
router=APIRouter(prefix="/user",tags=["users"])
@router.post('',response_model=schemas.ShowUser)
def create_user(request:schemas.User , db:Session=Depends(get_db)):
    return user.create(db,request)
@router.get('/{id}',response_model=schemas.ShowUser)
def get_user(id:int , db:Session=Depends(get_db)):
    return user.get(db,id)
