from fastapi import APIRouter
from app.api.health_router import health_router
from app.api.latest_data_router import latest_router
from app.api.history_data_router import history_router

routers = APIRouter()

routers.include_router(router=health_router, prefix="/health")
routers.include_router(router=latest_router, prefix="/latest")
routers.include_router(router=history_router, prefix="/history")
