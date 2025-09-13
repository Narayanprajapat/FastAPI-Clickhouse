from app.schemas.responses import LatestData
from fastapi import APIRouter, HTTPException, status
from app.services.latest_data_service import LatestDataService

latest_router = APIRouter()


@latest_router.get(
    path="/{symbol}",
    response_model=LatestData,
    status_code=status.HTTP_200_OK,
)
def latest_price(symbol: str):
    data = LatestDataService().get_latest_data(symbol=symbol)
    if not data:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"data not found for this stock {symbol}",
        )
    return data
