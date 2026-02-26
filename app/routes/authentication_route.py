from fastapi import (  # the apirouter works as traffic controller that handles the incoming web request and sent to the handler
    APIRouter,
    Depends,
    HTTPException,
    status,
)
from fastapi.security import OAuth2PasswordRequestForm
from fastapi_limiter.depends import RateLimiter
from pyrate_limiter import Duration, Limiter, Rate
from sqlalchemy.orm import Session

from app.authentication.jwt_creation import create_jwt_token, oauth
from app.authentication.password_hashing import check_hashed_password, create_hashed_password
from app.databse.db import get_db
from app.models.user_model import User

# from app.schema.user_login_schema import UserLogin
from app.schema.user_schema import CreateUser
from app.utilities.email_utility import send_mail

auth = APIRouter(prefix="/router", tags=["Authentication"])


@auth.post("/create")
def create_user(user: CreateUser, db: Session = Depends(get_db)):

    print("coming...")
    existing_user = db.query(User).filter(user.user_email == User.email).first()

    if existing_user:
        print("existing")
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, "user already exists")

    print("REGISTER PASSWORD EXACT:", repr(user.password))
    hashed_password = create_hashed_password(user.password)
    print(hashed_password)

    new_user = User(name=user.user_name, email=user.user_email, password=hashed_password)

    to = new_user.email
    subject = "account created successfully"
    body = f"the account is created succesfully with credentials : \n name : {new_user.name} , email : {new_user.email} "

    send_mail(to, subject, body)

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    # jwt_token = create_jwt_token(
    #     {
    #         "id" : new_user.id,
    #         "name" : new_user.name,
    #         "email" : new_user.email
    #     }
    # )
    print(
        {
            "status": "created",
            "id": new_user.id,
            "name": new_user.name,
            "email": new_user.email,
            # "token" : jwt_token
        }
    )
    return {
        "status": "created",
        "id": new_user.id,
        "name": new_user.name,
        "email": new_user.email,
        # "token" : jwt_token
    }


@auth.post("/login")
def login_user(db: Session = Depends(get_db), form_data: OAuth2PasswordRequestForm = Depends()):

    print("checking h ki ni")
    existing_user = db.query(User).filter(User.email == form_data.username).first()
    print("checked")
    print(existing_user)

    if not existing_user:
        print("not found...")
        raise HTTPException(status.HTTP_404_NOT_FOUND, "user not found")

    # check_pass = check_hashed_password(form_data.password, existing_user.password)
    # print("Testing against fresh hash...")
    # fresh_hash = create_hashed_password(form_data.password)
    # check_pass = check_hashed_password(form_data.password, existing_user.password)
    # print("RAW PASSWORD:", repr(form_data.password))
    # print("LENGTH:", len(form_data.password))
    # # print("user . name" , User.name)
    # print(User.email)
    # print("exis" , existing_user.name)
    # print("form" , form_data.username)
    # print(existing_user.password)
    # print(form_data.password)
    # print(check_pass)
    if not check_hashed_password(form_data.password, existing_user.password):
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, "Incorrect password")

    to = existing_user.email
    subject = "new login!!!"
    body = f"new login from your account : \n name : {existing_user.name} , email : {existing_user.email} "

    send_mail(to, subject, body)

    print("found")
    jwt_token = create_jwt_token(
        {
            "id": existing_user.id,
            "name": existing_user.name,
            "email": existing_user.email,
        }
    )

    return {"access_token": jwt_token, "token_type": "bearer"}


@auth.get(
    "/users", dependencies=[Depends(RateLimiter(limiter=Limiter(Rate(2, Duration.SECOND * 5))))]
)
def get_all_users(db: Session = Depends(get_db), token: str = Depends(oauth)):

    return db.query(User).all()


@auth.get(
    "/user-id:{entered_id}",
    dependencies=[Depends(RateLimiter(limiter=Limiter(Rate(2, Duration.SECOND * 5))))],
)
def get_user_by_id(entered_id: int, db: Session = Depends(get_db), token: str = Depends(oauth)):

    user = db.query(User).filter(User.id == entered_id).first()

    # return user

    return {
        "id": user.id,
        "name": user.name,
        "email": user.email,
        "created_at": user.created_at,
    }
