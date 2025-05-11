from fastapi import HTTPException,status
from sqlalchemy.orm import Session
import models
import schemas
def get_all(db:Session):
    blogs=db.query(models.Blog).all()
    return blogs
def create(db:Session,request:schemas.Blog):
    new_blog=models.Blog(title=request.title,body=request.body,user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog
def show(id:int,db:Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Blog with {id} not available')
    return blog
def destroy(id:int,db:Session):
    blog=db.query(models.Blog).filter(models.Blog.id==id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'Blog with {id} not available')
    blog.delete(synchronize_session=False)
    db.commit()
    return 'Deleted'