from pydantic import BaseModel


class AuthRegister(BaseModel):
    email: str
    username: str
    password: str


class AuthRegisterOutput(BaseModel):
    message: str
    username: str
    token: str
