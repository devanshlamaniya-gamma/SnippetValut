from fastapi import Depends , HTTPException , status
from app.databse.db import get_db , Base
from app.authentication.jwt_creation import create_jwt_token , check_jwt_token , oauth
from sqlalchemy.orm import Session
from app.models.user_model import User

def get_current_user(token:str = Depends(oauth) , db : Session= Depends(get_db)):


    payload = check_jwt_token(token)

    user_id = payload.get("user_id")

    if not user_id:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED , "token is invalid")
    
    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        return HTTPException(status.HTTP_404_NOT_FOUND , "user not found")
    
    return user
