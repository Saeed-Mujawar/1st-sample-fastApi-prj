from fastapi import APIRouter, Depends, status

from typing import List

from sqlalchemy.orm import Session

from blog import schemas, database, models

from blog.repository import blog

from blog import oaut2

router = APIRouter(
    tags=['blogs'],
    prefix="/blog"
)
get_db = database.get_db


@router.post('/', status_code= status.HTTP_201_CREATED)
def create(request: schemas.Blog,current_user_id: int ,db: Session = Depends(get_db), current_user: schemas.User = Depends(oaut2.get_current_user)):
    return blog.create(request,current_user_id ,db)

@router.delete('/{id}', status_code= status.HTTP_204_NO_CONTENT)
def delete(id: int, db: Session= Depends(get_db), current_user: schemas.User = Depends(oaut2.get_current_user)):
    return blog.delete(id, db)

@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update_blog(id: int, request: schemas.Blog, db: Session= Depends(get_db), current_user: schemas.User = Depends(oaut2.get_current_user)):
    return blog.update(id, request, db)


@router.get('/', response_model=List[schemas.ShowBlog])
def get_all_Blogs(db: Session = Depends(get_db), current_user: schemas.User = Depends(oaut2.get_current_user)):
    return blog.get_all_Blogs(db)

@router.get('/{id}', status_code=200, response_model=schemas.ShowBlog)
def get_by_id(id: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(oaut2.get_current_user)):
    return blog. get_by_id(id, db)