from clickhouse_pool import ChPool
from app.utils.logger import logging
from app.core.constants import (
    clickhouse_host,
    clickhouse_username,
    clickhouse_password,
    clickhouse_connections_max,
    clickhouse_connections_min,
)

logger = logging.getLogger(name="clickhouse.py")


class ClickhousePool:
    def __init__(self):
        self.pool = None
        self.client = None

    def connect(self):
        try:
            self.pool = ChPool(
                host=clickhouse_host,
                user=clickhouse_username,
                password=clickhouse_password,
                connections_min=clickhouse_connections_min,
                connections_max=clickhouse_connections_max,
            )
            self.client = self.pool.get_client()
            logger.info(msg="Clickhouse successfully connected")

        except Exception as e:
            logger.error(
                msg=f"Getting exception while trying to connect with clickhouse-{e}"
            )
            raise Exception(
                f"Getting exception while trying to connect with clickhouse-{e}"
            )

    def close_connection(self):
        self.pool.cleanup()
        self.pool = None
        self.client = None
        logger.info(msg="Clickhouse connection close")


clickhouse_pool = ClickhousePool()
