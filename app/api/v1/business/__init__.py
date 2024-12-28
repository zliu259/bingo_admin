from fastapi import APIRouter

from .business import router

business_router = APIRouter()
business_router.include_router(router, tags=["业务模块"])

__all__ = ["business_router"]
