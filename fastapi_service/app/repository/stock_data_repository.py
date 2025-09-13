from app.utils.logger import logging
from app.connection.clickhouse import clickhouse_pool
from app.schemas.responses import LatestData, HistoricalData


logger = logging.getLogger(name="stock_data_repository.py")


class StockDataRepository:
    def __init__(self):
        pass

    def create(self, stocks_info: list) -> None:
        with clickhouse_pool.client as client:
            insert_query = "INSERT INTO my_table (id, name, value) VALUES"
            client.execute(insert_query, stocks_info)
            logger.info(msg=f"Data inserted successfully. {len(stocks_info)}")

    def get_latest_by_symbol(self, symbol: str) -> LatestData:
        with clickhouse_pool.client as client:
            result = client.execute("SELECT * FROM system.numbers LIMIT 5")
            print(result)

    def get_all_by_symbol(self, symbol: str) -> list[HistoricalData]:
        with clickhouse_pool.client as client:
            result = client.execute("SELECT * FROM system.numbers LIMIT 5")
            print(result)
