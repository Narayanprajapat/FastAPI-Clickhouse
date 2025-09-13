from app.utils.logger import logging
from app.connection.clickhouse import clickhouse_pool
from app.schemas.responses import LatestData, HistoricalData


logger = logging.getLogger(name="stock_data_repository.py")


class StockDataRepository:
    def __init__(self):
        pass

    def get_latest_by_symbol(self, symbol: str) -> LatestData:
        with clickhouse_pool.pool.get_client() as client:
            result = client.execute(
                f"SELECT event_time, symbol, open, close FROM market.ticks WHERE symbol='{symbol}' ORDER BY event_time DESC LIMIT 1"
            )
            if result:
                record = LatestData(
                    last_updated=result[0][0],
                    symbol=result[0][1],
                    open=result[0][2],
                    close=result[0][3],
                )
                return record
            return None

    def get_all_by_symbol(self, symbol: str) -> list[HistoricalData]:
        with clickhouse_pool.pool.get_client() as client:
            results = client.execute(
                f"SELECT symbol, date, open, close, high, low, volume FROM market.ticks WHERE symbol='{symbol}'"
            )
            return [
                HistoricalData(
                    symbol=result[0],
                    date=result[1],
                    open=result[2],
                    close=result[3],
                    high=result[4],
                    low=result[5],
                    volume=result[6],
                )
                for result in results
                if results
            ]
