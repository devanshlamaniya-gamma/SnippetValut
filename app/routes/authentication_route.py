from fastapi import status , HTTPException , Depends , APIRouter  # the apirouter works as traffic controller that handles the incoming web request and sent to the handler
from sqlalchemy.orm import Session

from app.authentication.jwt_creation import check_jwt_token , create_jwt_token , oauth
from app.schema.user_schema import CreateUser
from app.models.user_model import User
from app.databse.db import get_db
from fastapi.security import OAuth2PasswordRequestForm
import bcrypt


from app.schema.user_login_schema import UserLogin

from app.authentication.password_hashing import create_hashed_password , check_hashed_password

auth = APIRouter(prefix="/router" , tags= ["Authentication"])

@auth.post("/create")
def create_user(user : CreateUser , db : Session = Depends(get_db)):

    print("coming...")
    existing_user = db.query(User).filter(user.user_email == User.email).first()


    if existing_user:
        print("existing")
        raise HTTPException(status.HTTP_401_UNAUTHORIZED)
    
    hashed_password = create_hashed_password(str(user.password))

    new_user = User(
    
        name = user.user_name,
        email = user.user_email,
        password = hashed_password
    )
 
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

    return {
        "status" : "created",
        "id" : new_user.id,
        "name" : new_user.name,
        "email" : new_user.email,
        # "token" : jwt_token
    }


@auth.post("/login")
def login_user( db : Session = Depends(get_db) , form_data :OAuth2PasswordRequestForm = Depends() ):

    print("checking h ki ni")
    existing_user = db.query(User).filter(form_data.username == User.name).first()
    print("checked")
    print(existing_user)

    if not existing_user:
        print("not found...")
        raise HTTPException(status.HTTP_404_NOT_FOUND , "user not found")
    
    print("found")
    jwt_token = create_jwt_token ({
        "id" : existing_user.id,
        "name" : existing_user.name,
        "email" : existing_user.email
    })

    return{
        "access_token" : jwt_token,
        "token_type" : "bearer"
    }
    

@auth.get("/users")
def get_all_users(db : Session = Depends(get_db) , token : str = Depends(oauth)):

    return db.query(User).all()

@auth.get("/user-id:{id}")
def get_user_by_id(entered_id : int , db : Session=Depends(get_db)):

    user =  db.query(User).filter(User.id == entered_id).first()

    # return user

    return {
        "id" : user.id,
        "name" : user.name,
        "email" : user.email,
        "created_at" : user.created_at
    }   