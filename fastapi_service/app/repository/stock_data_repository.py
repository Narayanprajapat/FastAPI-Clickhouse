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
                f"SELECT event_time, symbol, open, close FROM market.ticks WHERE symbol='{symbol}' ORDER BY event_time ASC LIMIT 1"
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
            result = client.execute("SELECT * FROM system.numbers LIMIT 5")
            print(result)
