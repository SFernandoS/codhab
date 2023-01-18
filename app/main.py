from fastapi import FastAPI
from app.databases import engine
from app.user import models, main
import os


metadata_tags = [
    {'name':"Users", 'description': "These are the users"},
]

if os.getenv("API_ENV") != 'test':
    models.Base.metadata.create_all(bind=engine)

app = FastAPI(openapi_tags=metadata_tags)

app.include_router(main.router)
