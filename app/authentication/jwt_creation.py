import os
from dotenv import load_dotenv
load_dotenv()

from fastapi.security import OAuth2PasswordBearer

from datetime import datetime , timedelta , timezone

oauth = OAuth2PasswordBearer(tokenUrl="/router/login")

import jwt

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = "HS256"
EXPIRATION_TIME_MINS = 15

def create_jwt_token(data : dict):

    data_to_encode = data.copy()

    expire = datetime.now(timezone.utc) + timedelta(minutes=EXPIRATION_TIME_MINS)

    data_to_encode.update({"exp" : expire})

    jwt_token = jwt.encode(data_to_encode , SECRET_KEY , ALGORITHM)

    return jwt_token

# print(create_jwt_token({"name" : "devansh" , "password" : "devansh123"}))

def check_jwt_token(token:str):

    try :
        payload = jwt.decode(token , SECRET_KEY ,ALGORITHM)
        
        return payload

    except jwt.ExpiredSignatureError:
        return ("the token is expired")
    
    except jwt.InvalidTokenError:
        return ("the token is invalid")
    
# print(check_jwt_token("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoiZGV2YW5zaCIsInBhc3N3b3JkIjoiZGV2YW5zaDEyMyIsImV4cGlyZSI6IjIwMjYtMDItMTcgMTI6NTk6NTUuNzU0NzM2In0.HfAuN5Uf0zx0HdoJLZVZyXeB_YDAFiUx0t-BGb12cBY"))