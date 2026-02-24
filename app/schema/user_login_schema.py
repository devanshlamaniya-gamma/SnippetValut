from pydantic import BaseModel, EmailStr


class UserLogin(BaseModel):
    email: EmailStr
    password: str


#the pydantic is the module and the basemodel is the class  that checks the input values that they are correct or not this ensure that the input will be in correct form