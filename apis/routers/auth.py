from fastapi import APIRouter, HTTPException, status

from controllers.auth import AuthCRUD
from dependencies import SessionDep
from schemas.auth import AuthRegister, AuthRegisterOutput
from utils.security import generate_token

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
            "username": new_user.email,
            "token": user_token,
        }
