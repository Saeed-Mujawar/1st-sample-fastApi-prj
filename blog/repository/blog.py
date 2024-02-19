from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from blog import models,schemas






def get_all_Blogs(db: Session):
    blogs = db.query(models.Blog).all()

    return blogs

def create(request:schemas.Blog, current_user_id: int, db: Session):
    new_blog = models.Blog(title=request.title, body=request.body, user_id= current_user_id)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)

    return new_blog

def delete(id: int, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)

    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} not found")

    blog.delete(synchronize_session=False)
    db.commit()

    return {f'ID {id} is Deleted'}

# synchronize_session=False: is an argument passed to the delete() method.
# When set to False, it instructs SQLAlchemy not to synchronize the changes made by the deletion operation with the session.
# This means that SQLAlchemy will not automatically remove the deleted object from the session's identity map, which can improve performance when deleting large numbers of objects.

def update(id: int, request: schemas.Blog, db: Session):

    blog = db.query(models.Blog).filter(models.Blog.id == id).first()

    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} not found")

    for attr, value in request.dict().items():
        setattr(blog, attr, value)

    db.commit()

    return "updated successfully"

# explaination for 'for' loop in update request
# We are iterating over the items of the dictionary representation of the request object using the items() method, which returns a key-value pair for each item in the dictionary.
# request.dict(): This method converts the request object (which is likely a Pydantic model instance) into a dictionary representation
# The object whose attribute we want to set (in this case, blog).
# The name of the attribute we want to set (stored in the attr variable).
# The value we want to set for the attribute (stored in the value variable).

def get_by_id(id, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"blog with ID {id} not available")
  
    return blog