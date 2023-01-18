from fastapi import FastAPI
from databases import engine
from user import models, main

models.Base.metadata.create_all(bind=engine)


metadata_tags = [
    {'name':"Users", 'description': "These are the users"},
]

app = FastAPI(openapi_tags=metadata_tags)

app.include_router(main.router)