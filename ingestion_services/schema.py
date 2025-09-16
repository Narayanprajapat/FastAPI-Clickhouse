from pydantic import BaseModel
from datetime import date, datetime


class Stock(BaseModel):
    event_time: datetime
    date: date
    symbol: str
    open: float
    high: float
    low: float
    close: float
    volume: int
    prev_close_price: float
