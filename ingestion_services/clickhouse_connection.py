from clickhouse_pool import ChPool

clickhouse_connections_min = 1
clickhouse_connections_max = 5

clickhouse_host = "localhost"
clickhouse_username = "default"
clickhouse_password = "1234"


class ClickhousePool:
    def __init__(self):
        self.pool = None
        self.connect()

    def connect(self):
        try:
            self.pool = ChPool(
                host=clickhouse_host,
                user=clickhouse_username,
                password=clickhouse_password,
                connections_min=clickhouse_connections_min,
                connections_max=clickhouse_connections_max,
            )
            print("Clickhouse successfully connected")

        except Exception as e:
            print(f"Getting exception while trying to connect with clickhouse-{e}")
            raise Exception(
                f"Getting exception while trying to connect with clickhouse-{e}"
            )

    def close_connection(self):
        self.pool.cleanup()
        self.pool = None
        print("Clickhouse connection close")


clickhouse_pool = ClickhousePool()
