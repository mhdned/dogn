from typing import Union

from pydantic import BaseModel, EmailStr


class AuthRegister(BaseModel):
    email: EmailStr
    username: str
    password: str


class AuthRegisterOutput(BaseModel):
    message: str
    email: str
    token: str


class AuthEntrance(BaseModel):
    email_or_username: Union[EmailStr, str]
    password: str


class AuthEntranceOutput(BaseModel):
    message: str
    email: str
    token: str
