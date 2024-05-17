from fastapi import APIRouter

router = APIRouter()

# import sub routings
from apis.routers.auth import router as AuthRouter
from apis.routers.document import router as DocumentRouter
from apis.routers.root import router as RootRouter
from apis.routers.signature import router as SignatureRouter
from apis.routers.user import router as UserRouter

router.include_router(router=RootRouter, prefix="", tags=["root"])
router.include_router(router=AuthRouter, prefix="/auth", tags=["auth"])
router.include_router(router=UserRouter, prefix="/user", tags=["user"])
router.include_router(router=DocumentRouter, prefix="/document", tags=["document"])
router.include_router(router=SignatureRouter, prefix="/signature", tags=["signature"])
