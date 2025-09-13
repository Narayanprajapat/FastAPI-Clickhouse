from app.schemas.responses import LatestData
from app.repository.stock_data_repository import StockDataRepository


class LatestDataService:
    def __init__(self):
        pass

    def get_latest_data(self, symbol: str) -> LatestData:
        return StockDataRepository().get_latest_by_symbol(symbol=symbol)
