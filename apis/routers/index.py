from fastapi import APIRouter

router = APIRouter()

from apis.routers.auth import router as AuthRouter

# import sub routings
from apis.routers.root import router as RootRouter

router.include_router(router=RootRouter, prefix="", tags=["root"])
router.include_router(router=AuthRouter, prefix="/auth", tags=["auth"])
