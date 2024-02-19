from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from blog.hashing import Hash

from blog import models,schemas

def create_user(request: schemas.User, db: Session):
    new_user = models.User(username = request.username, email=request.email, password= Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_User_By_Id(id: int, db: Session):
    user = db.query(models.User).filter(models.User.id == id).first()

    if not user:
         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"user with ID {id} not available")
    return user
  
def get_all_Users(db: Session):
    user = db.query(models.User).all()
    return user
