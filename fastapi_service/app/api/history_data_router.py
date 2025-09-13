from fastapi import APIRouter, status
from app.schemas.responses import HistoricalData
from app.services.history_data_service import HistoryDataService

history_router = APIRouter()


@history_router.get(
    path="/{symbol}",
    response_model=HistoricalData,
    status_code=status.HTTP_200_OK,
)
async def latest_price(symbol: str):
    return HistoryDataService.get_all_data(symbol=symbol)
