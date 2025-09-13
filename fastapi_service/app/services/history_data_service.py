from app.schemas.responses import HistoricalData
from app.repository.stock_data_repository import StockDataRepository


class HistoryDataService:
    def __init__(self):
        pass

    def get_all_data(self, symbol: str) -> HistoricalData:
        return StockDataRepository().get_all_by_symbol(symbol=symbol)
