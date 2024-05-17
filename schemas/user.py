from datetime import datetime
from typing import Union

from pydantic import BaseModel


class User(BaseModel):
    id: int
    username: str
    email: str
    created_at: Union[datetime, None]


class UserList(BaseModel):
    message: str
    users: list[User]
