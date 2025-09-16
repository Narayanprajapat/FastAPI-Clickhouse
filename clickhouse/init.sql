CREATE DATABASE IF NOT EXISTS market;

CREATE TABLE IF NOT EXISTS market.ticks
(
    event_time   DateTime,
    date         Date,
    symbol       String,
    open         Float64,
    high         Float64,
    low          Float64,
    close        Float64,
    volume       UInt64,
    prev_close_price Float64,
    created_at   DateTime DEFAULT now()
)
ENGINE = MergeTree()
PARTITION BY toYYYYMM(date)
ORDER BY (symbol, event_time);