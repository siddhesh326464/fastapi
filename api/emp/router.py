from fastapi import APIRouter
from api.emp.controller import router

api_router = APIRouter()
api_router.include_router(router,tags=["auth"])
