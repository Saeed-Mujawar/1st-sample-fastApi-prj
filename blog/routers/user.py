
from typing import List

from fastapi import APIRouter, Depends, status, HTTPException

from sqlalchemy.orm import Session

from blog import schemas, database, models



from blog.repository import user

router = APIRouter(
    tags=['users'],
    prefix="/user"
)
get_db = database.get_db

@router.post("/", response_model= schemas.ShowUser)
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    return user.create_user(request, db)

@router.get('/{id}', response_model= schemas.ShowUser)
def get_User_By_Id(id: int, db: Session = Depends(get_db)):
    return user.get_User_By_Id(id, db)

@router.get('/', response_model=List[schemas.ShowUser])
def get_all_Users(db: Session = Depends(get_db)):
    return user.get_all_Users(db)
  
