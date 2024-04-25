from fastapi import APIRouter, HTTPException, status

from controllers.auth import AuthCRUD
from dependencies import SessionDep
from models import User
from schemas.auth import (
    AuthEntrance,
    AuthEntranceOutput,
    AuthRegister,
    AuthRegisterOutput,
)
from utils.security import compare_passwords, generate_token

router = APIRouter()


@router.post(
    path="/register",
    status_code=status.HTTP_201_CREATED,
    response_model=AuthRegisterOutput,
)
def create_user(user: AuthRegister, db: SessionDep):
    auth_crud = AuthCRUD(session=db)
    is_email_exist = auth_crud.find_user_by_email(user.email)
    if is_email_exist:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"The email <{user.email}> already been registered",
        )
    else:
        new_user = auth_crud.create_user(user)
        user_token = generate_token({"username": new_user.username})
        return {
            "message": "User register successfully",
            "email": new_user.email,
            "token": user_token,
        }


@router.post(
    path="/entrance", status_code=status.HTTP_200_OK, response_model=AuthEntranceOutput
)
async def entrance_user(user: AuthEntrance, db: SessionDep):
    auth_crud = AuthCRUD(session=db)
    current_user: User
    if "@" in user.email_or_username:
        email = user.email_or_username
        # Authenticate using email
        current_user = auth_crud.find_user_by_email(email)

    else:
        username = user.email_or_username
        # Authenticate using username
        current_user = auth_crud.find_user_by_username(username)

    if current_user:
        # Check password is valid
        if compare_passwords(user.password, current_user.password):
            user_token = generate_token({"username": current_user.username})
            return {
                "message": "User entrance successfully",
                "email": current_user.email,
                "token": user_token,
            }
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Password is invalid, try again",
            )
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"There is no user with this <{user.email_or_username}> username or email, we suggest to you use email for entrance",
        )
