from pydantic import BaseModel, Field, field_validator
from typing import Optional
from datetime import datetime


class UserLoginSchema(BaseModel):
    username: str = Field(..., max_length=250, description="Username of the user")
    password: str = Field(..., description="Password of the user")


class UserRegisterSchema(BaseModel):
    username: str = Field(..., max_length=250, description="Username of the user")
    password: str = Field(..., description="Password of the user")
    password_confirm: str = Field(..., description="Confirm password of the user")

    @field_validator("password_confirm")
    def check_passwords_match(cls, password_confirm, validation):
        if not (password_confirm == validation.data.get("password")):
            raise ValueError("Password doesnt match")

        return password_confirm
