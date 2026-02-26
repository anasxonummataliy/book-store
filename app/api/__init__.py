from fastapi import APIRouter
from app.api.router import router as book_router

routers = APIRouter()
routers.include_router(book_router)
