from pydantic import BaseModel
from datetime import date, datetime


class StockInfo(BaseModel):
    symbol: str
    close: float
    open: float


class LatestData(StockInfo):
    last_updated: datetime


class HistoricalData(StockInfo):
    date: date
    high: float
    low: float
    volume: int


class Response(BaseModel):
    message: str
    status_code: int
