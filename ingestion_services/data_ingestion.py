import datetime
from fyers_apiv3.FyersWebsocket import data_ws


from schema import Stock
from config import fyers_config
from clickhouse_connection import clickhouse_pool


class FyersWebSocketClient:

    def __init__(self, client_id: str, access_token: str, symbols: list):
        self.final_token = f"{client_id}:{access_token}"
        self.symbols = symbols

        self.fyers = data_ws.FyersDataSocket(
            access_token=self.final_token,
            log_path="",
            litemode=False,
            write_to_file=False,
            reconnect=True,
            on_connect=self.on_open,
            on_close=self.on_close,
            on_error=self.on_error,
            on_message=self.on_message,
        )

    def inserting_into_clickhouse(self, values: list) -> None:
        try:
            with clickhouse_pool.pool.get_client() as client:
                query = """
                    INSERT INTO 
                        market.ticks (
                            event_time, 
                            date, 
                            symbol, 
                            open, 
                            high, 
                            low, 
                            close, 
                            volume, 
                            prev_close_price
                        ) 
                    VALUES
                """
                client.execute(query, values)

            print("data inserted sucessfully into clickhouse")
        except Exception as e:
            print("Exception occurred--", e)

    def data_processing(self, raw_data: dict) -> list:
        ts = raw_data["last_traded_time"]
        dt_local = datetime.datetime.fromtimestamp(ts)
        info = {
            "symbol": raw_data["symbol"].replace("NSE:", "").replace("-EQ", ""),
            "date": dt_local.date(),
            "event_time": dt_local,
            "open": raw_data["open_price"],
            "close": raw_data["ltp"],
            "low": raw_data["low_price"],
            "high": raw_data["high_price"],
            "volume": raw_data["vol_traded_today"],
            "prev_close_price": raw_data["prev_close_price"],
        }

        stock_info = Stock(**info).dict()

        values = [
            (
                stock_info["event_time"],
                stock_info["date"],
                stock_info["symbol"],
                stock_info["open"],
                stock_info["high"],
                stock_info["low"],
                stock_info["close"],
                stock_info["volume"],
                stock_info["prev_close_price"],
            )
        ]
        return values

    def on_message(self, message):
        print("Response:", message)
        try:
            if "type" in message and message["type"] == "sf":
                values = self.data_processing(raw_data=message)
                self.inserting_into_clickhouse(values=values)
        except Exception as e:
            print("Exception", e)

    def on_error(self, message):
        print("Error:", message)

    def on_close(self, message):
        print("Connection closed:", message)

    def on_open(self):
        print("WebSocket Connected. Subscribing to symbols...")
        data_type = "SymbolUpdate"

        self.fyers.subscribe(symbols=self.symbols, data_type=data_type)
        self.fyers.keep_running()

    def connect(self):
        print("Connecting to Fyers WebSocket...")
        self.fyers.connect()


def main() -> None:
    symbols = [
        "NSE:RELIANCE-EQ",
        "NSE:TCS-EQ",
        "NSE:INFY-EQ",
        "NSE:HDFCBANK-EQ",
        "NSE:ICICIBANK-EQ",
        "NSE:SBIN-EQ",
        "NSE:AXISBANK-EQ",
        "NSE:KOTAKBANK-EQ",
        "NSE:BAJFINANCE-EQ",
        "NSE:ITC-EQ",
        "NSE:HINDUNILVR-EQ",
        "NSE:LT-EQ",
        "NSE:ADANIENT-EQ",
        "NSE:ADANIPORTS-EQ",
        "NSE:WIPRO-EQ",
        "NSE:HCLTECH-EQ",
        "NSE:TECHM-EQ",
        "NSE:MARUTI-EQ",
        "NSE:M&M-EQ",
        "NSE:TATAMOTORS-EQ",
        "NSE:TITAN-EQ",
        "NSE:ONGC-EQ",
        "NSE:NTPC-EQ",
        "NSE:POWERGRID-EQ",
    ]

    ws_client = FyersWebSocketClient(
        client_id=fyers_config.CLIENT_ID,
        access_token=fyers_config.ACCESS_TOKEN,
        symbols=symbols,
    )
    ws_client.connect()


if __name__ == "__main__":
    main()
