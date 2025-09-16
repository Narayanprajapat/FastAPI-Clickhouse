from pydantic_settings import BaseSettings


class FyersConfig(BaseSettings):
    CLIENT_ID: str
    ACCESS_TOKEN: str

    class Config:
        env_file = ".env"


fyers_config = FyersConfig()
