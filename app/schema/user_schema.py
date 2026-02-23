import re
from typing import Annotated

from pydantic import BaseModel, EmailStr, Field, field_validator


class CreateUser(BaseModel):

    user_name: Annotated[str, Field(..., description="user_name")]
    user_email: Annotated[EmailStr, Field(..., description="user email")]
    password: Annotated[str, Field(..., min_length=8, description="user password")]

    @field_validator("password")
    def strong_password(cls, password):
        if not re.search(r"[A-Z]", password):
            raise ValueError("password must contain at least 1 upper case ")

        if not re.search(r"[a-z]", password):
            raise ValueError("password must contain at least 1 small case")

        if not re.search(r"\d", password):
            raise ValueError("password must contain at least 1 digit")

        if not re.search(r'[!@#$%^&*(),.?":{}|<>-]', password):
            raise ValueError("password must contain at least 1 special character")
