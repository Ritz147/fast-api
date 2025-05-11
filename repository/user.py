import models
from sqlalchemy.orm import Session
import hashing
import schemas
from fastapi import HTTPException,status
def create(db:Session , request:schemas.User):
    hashed_password=hashing.Hash.bcrypt(request.password)
    new_user=models.User(name=request.name,email=request.email,password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
def get(db:Session , id:int):
    user=db.query(models.User).filter(models.User.id==id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'User with {id} not available')
    return user