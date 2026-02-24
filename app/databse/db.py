import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)  # this helps to connect with db

local_session = sessionmaker(bind=engine, autoflush=False, autocommit=False)
Base = declarative_base()  # this class contains metadata object where newly defned table are collected
print(Base.metadata.tables.keys())
print(Base.metadata.tables.values())


def get_db():

    db = local_session()

    try:
        yield db

    finally:
        db.close()
