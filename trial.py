from app.databse.db import get_db   , local_session
from fastapi import Depends
from sqlalchemy.orm import Session
from app.schema.user_schema import CreateUser
from app.models.user_model import User


def testing(user : CreateUser , db : Session = Depends(get_db)):

    existing = db.query(User).filter(User.name == user.user_name).first()

    if not existing:
        print("user is not present")

    u = User(name = "devansh" , password = "devansh123")
    