import time
import yfinance as yf
from datetime import datetime
from clickhouse_connection import clickhouse_pool


tickers = [
    "RELIANCE.NS",  # Reliance Industries
    "TCS.NS",  # Tata Consultancy Services
    "HDFCBANK.NS",  # HDFC Bank
    "INFY.NS",  # Infosys
    "SBIN.NS",  # State Bank of India
    "HINDUNILVR.NS",  # Hindustan Unilever
    "BAJAJFINSV.NS",  # Bajaj Finserv
    "ONGC.NS",  # Oil and Natural Gas Corp
    "NTPC.NS",  # NTPC Limited
    "TITAN.NS",  # Titan Company
]


def fetch_prices():
    data = []
    for t in tickers:
        stock = yf.Ticker(t)
        info = stock.fast_info
        now = datetime.now()
        try:
            json_output = {
                "event_time": now,
                "date": now.date(),
                "symbol": t.replace(".NS", ""),
                "open": float(info["open"]),
                "high": float(info["day_high"]),
                "low": float(info["day_low"]),
                "close": float(info["last_price"]),
                "volume": int(info["last_volume"]),
            }
            data.append(json_output)
        except Exception as e:
            print(f"Exception occurred {e} for {t}")

    insert_values = [
        (
            d["event_time"],
            d["date"],
            d["symbol"],
            d["open"],
            d["high"],
            d["low"],
            d["close"],
            d["volume"],
        )
        for d in data
    ]

    print("data fetched succesfully")

    with clickhouse_pool.pool.get_client() as client:
        insert_query = "INSERT INTO market.ticks (event_time, date, symbol, open, high, low, close, volume) VALUES"

        client.execute(insert_query, insert_values)

    print("data inserted sucessfully into clickhouse")


def main() -> None:
    while True:
        fetch_prices()
        time.sleep(5)


if __name__ == "__main__":
    main()
