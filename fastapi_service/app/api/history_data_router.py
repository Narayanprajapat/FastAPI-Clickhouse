from app.schemas.responses import HistoricalData
from fastapi import APIRouter, HTTPException, status
from app.services.history_data_service import HistoryDataService

history_router = APIRouter()


@history_router.get(
    path="/{symbol}",
    response_model=list[HistoricalData],
    status_code=status.HTTP_200_OK,
)
async def latest_price(symbol: str):
    data = HistoryDataService().get_all_data(symbol=symbol)
    if not data:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"data not found for this stock {symbol}",
        )
    return data
