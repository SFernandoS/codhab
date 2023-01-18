from fastapi import FastAPI, Depends, status
from sqlalchemy.orm import Session
from databases import engine
from dependencies import get_db
import models as models
import schemas as schemas


app = FastAPI()
models.Base.metadata.create_all(bind=engine)
metadata_tags = [
    {'name':"Users", 'description': "These are the users"},
]


@app.get("/", status_code=status.HTTP_200_OK)
def welcome():
    return {'Welcome to codhab api!'}


@app.get("/user", status_code=status.HTTP_200_OK, tags=["Users"])
def read_all_users(db: Session = Depends(get_db)):
    return {'users':[ users.json() \
        for users in db.query(models.User).all()]}

@app.post("/user", status_code=status.HTTP_201_CREATED, tags=["Users"])
def create_user(create_user: schemas.UserSchema, db: Session = Depends(get_db)):
    create_user_model = models.User()
    create_user_model.cpf = create_user.cpf
    create_user_model.nome = create_user.nome
    create_user_model.email = create_user.email
    create_user_model.telefone = create_user.telefone

    db.add(create_user_model)
    db.commit()

    return {
        'status': 201,
        'transaction': 'Successful'
    }
