from fastapi import APIRouter, status
from app.schemas.responses import LatestData
from app.services.latest_data_service import LatestDataService

latest_router = APIRouter()


@latest_router.get(
    path="/{symbol}",
    response_model=LatestData,
    status_code=status.HTTP_200_OK,
)
async def latest_price(symbol: str):
    return LatestDataService.get_latest_data(symbol=symbol)
