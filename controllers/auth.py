from pydantic import EmailStr
from sqlalchemy.orm import Session

from models import User
from schemas.auth import AuthRegister
from utils.security import hash_password


class AuthCRUD:
    def __init__(self, session: Session):
        self.session = session

    def create_user(self, user_data: AuthRegister):
        password_hashed = hash_password(user_data.password)
        new_user = User(
            username=user_data.username,
            email=user_data.email,
            password=password_hashed,
        )
        self.session.add(new_user)
        self.session.commit()
        self.session.refresh(new_user)
        return new_user

    def find_user_by_email(self, email: EmailStr):
        return self.session.query(User).filter(User.email == email).first()

    def find_user_by_username(self, username: str):
        return self.session.query(User).filter(User.username == username).first()
