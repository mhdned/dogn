from fastapi import APIRouter, HTTPException, status

# CRUD
from controllers.user import UserCRUD

# Session
from dependencies import SessionDep

# Schemas
from schemas.user import UserList

# Definition instance of APIRouter
router = APIRouter()


@router.get("/all", status_code=status.HTTP_200_OK, response_model=UserList)
async def find_users(db: SessionDep):
    user_crud = UserCRUD(session=db)
    users = user_crud.read_all_user()
    if users:
        if len(users) > 0:
            return {"message": "Users found successfully", "users": users}
        else:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="It does not register any user in the system",
            )
    else:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Something wrong about fetching data from database, please try later",
        )
