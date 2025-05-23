from fastapi import APIRouter,Depends,HTTPException,status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
import database
import schemas
import models
import hashing
import auth_token
router=APIRouter(tags=["Authentication"])
@router.post('/login',response_model=schemas.Token)
def login( request:OAuth2PasswordRequestForm= Depends(),db:Session=Depends(database.get_db)):
    user=db.query(models.User).filter(models.User.email==request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'User with the given username or password is not available')
    if not hashing.Hash.verify(user.password,request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Incorrect Password')
    #return a jwtToken and return 
    access_token = auth_token.create_access_token(
        data={"sub": user.email}
    )
    return {"access_token":access_token, "token_type":"bearer"}