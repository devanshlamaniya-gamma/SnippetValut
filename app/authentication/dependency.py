import json

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from app.authentication.jwt_creation import check_jwt_token, create_jwt_token, oauth
from app.databse.db import Base, get_db
from app.models.user_model import User

# def get_current_user(token:dict = Depends(oauth) , db : Session= Depends(get_db)):


#     payload = check_jwt_token(token)
#     print(type(payload))

#     # if isinstance(payload, str):

#     #     payload = json.loads(payload)

#     # print(payload)
#     # print(type(payload))
#     user_id = payload.get("id")

#     if not user_id:
#         raise HTTPException(status.HTTP_401_UNAUTHORIZED , "token is invalid")

#     user = db.query(User).filter(User.id == user_id).first()

#     if not user:
#         return HTTPException(status.HTTP_404_NOT_FOUND , "user not found")

#     return user_id


def get_current_user(token: str = Depends(oauth), db: Session = Depends(get_db)):

    print("type of token", type(token))
    print("token: ", token)

    payload = check_jwt_token(token)
    print("type of payload", type(payload))
    print("this is payload", payload)

    user_id = payload.get("id")
    if not user_id:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, "User ID missing in token")

    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "User not found")

    return user
