import os
from dotenv import load_dotenv
load_dotenv()
from fastapi import HTTPException , status
from fastapi.security import OAuth2PasswordBearer

from datetime import datetime , timedelta , timezone

oauth = OAuth2PasswordBearer(tokenUrl="/router/login")

import jwt

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = "HS256"
EXPIRATION_TIME_MINS = 90

def create_jwt_token(data : dict):

    data_to_encode = data.copy()

    expire = datetime.now() + timedelta(minutes=EXPIRATION_TIME_MINS)

    data_to_encode.update({"exp" : expire})

    jwt_token = jwt.encode(data_to_encode , SECRET_KEY , ALGORITHM)

    return jwt_token

# print(create_jwt_token({"name" : "devansh" , "password" : "devansh123"}))

def check_jwt_token(token:str):

    print("this is the token",token)
    try :
        payload = jwt.decode(token , SECRET_KEY ,algorithms=[ALGORITHM])
        print(type(payload))
        
        return payload

    except jwt.ExpiredSignatureError:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED , "token is expired")
    
    except jwt.InvalidTokenError as e:
        print(f"JWT Error: {e}") 
        raise HTTPException(status.HTTP_401_UNAUTHORIZED , "invalid token ")
    
