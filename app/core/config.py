from pydantic_settings import BaseSettings


class ClickhouseSettings(BaseSettings):
    HOST: str
    USERNAME: str
    PASSWORD: str


clickhouse_settings = ClickhouseSettings()
