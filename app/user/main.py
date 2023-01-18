from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from app.dependencies import get_db
from app.user import models, schemas

router = APIRouter()


@router.get("/", status_code=status.HTTP_200_OK)
def welcome():
    return {'Welcome to codhab api!'}


@router.get("/user", status_code=status.HTTP_200_OK, tags=["Users"])
def read_all_users(db: Session = Depends(get_db)):
    return {'users': [users.json() for users in db.query(models.User).all()]}


@router.post("/user", status_code=status.HTTP_201_CREATED, tags=["Users"])
def create_user(create_user: schemas.UserSchema,
                db: Session = Depends(get_db)):

    create_user_model = models.User(**create_user.dict())

    db.add(create_user_model)
    db.commit()

    return {
        'status': 201,
        'transaction': 'Successful'
    }


@router.delete("/user/{id}", status_code=status.HTTP_200_OK, tags=["Users"])
def delete_user(id, db: Session = Depends(get_db)):

    user = db.query(models.User).get(id)

    if user:
        db.delete(user)
        db.commit()

    return {
        'status': 200,
        'transaction': 'User deleted'
    }


@router.put("/user/{id}", status_code=status.HTTP_200_OK, tags=["Users"])
def put_user(id, userSchema: schemas.UserSchema,
             db: Session = Depends(get_db)):

    user = db.query(models.User).get(id)

    if user:
        models.User.set_user(user, **userSchema.dict())
        db.commit()
        if not user:
            raise HTTPException(status_code=404, detail="User not found!")

        return {
            'status': 200,
            'transaction': 'Changed'
        }
