
import os

os.environ['POSTGRES_USER'] = 'postgres'
os.environ['POSTGRES_PASSWORD'] = 'password'
os.environ['POSTGRES_DB'] = 'codhab-dev'
os.environ['POSTGRES_PORT'] = '5432'
os.environ['POSTGRES_HOST'] = 'codhab-db'
os.environ['API_ENV'] = 'test'

from fastapi.testclient import TestClient

from app.databases import Base
from app.dependencies import get_db
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.main import app

SQLALCHEMY_DATABASE_URL = "sqlite:///test.db"


engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False,
                                   autoflush=False, bind=engine)


Base.metadata.create_all(bind=engine)


def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)

user = {"cpf": "12345678910", "nome": "Junior da Silva",
        "email": "junior@email.com", "telefone": "61912345678"}
user = {"cpf": "10987654321", "nome": "Maria de Jesus",
        "email": "maria@email.com", "telefone": "61912345678"}


def test_welcome():
    response = client.get("/")
    assert response.status_code == 200


def test_create_user():
    response = client.post("/user", json=user)
    assert response.status_code == 201


def test_delete_user():
    client.post("/user", json=user)
    response = client.delete("/user/1")
    assert response.status_code == 200


def test_update_user():
    client.post("/user", json=user)
    response = client.put("/user/1", json=user)
    assert response.status_code == 200
