from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os


DATABASE_URL = f"postgresql://{os.getenv('POSTGRES_USER')}:"\
               f"{os.getenv('POSTGRES_PASSWORD')}@"\
               f"{os.getenv('POSTGRES_HOST')}:"\
               f"{os.getenv('POSTGRES_PORT')}/"\
               f"{os.getenv('POSTGRES_DB')}"


engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
