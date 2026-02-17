from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base , sessionmaker

import os

from dotenv import load_dotenv

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)       # this helps to connect with db

local_session = sessionmaker(bind = engine , autoflush=False , autocommit = False)     # this makes temp access to db so we can do operations we make new session every time 

Base = declarative_base()       # this class contains metadata object where newly defned table are collected

def get_db():

    db = local_session()

    try:
        yield db

    finally:
        db.close()

from sqlalchemy import text

if __name__ == "__main__":
    try:
        with engine.connect() as connection:
            result = connection.execute(text("select 1"))
            print("connection successful")
    except Exception as e:
        print("test connection failed " , e)