from dotenv import load_dotenv

load_dotenv()
from time import time
from fastapi import FastAPI, Request
from contextlib import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware

from app.api import routers
from app.utils.logger import logging
from app.connection.clickhouse import clickhouse_pool


logger = logging.getLogger(name="server.py")


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Starting")
    clickhouse_pool.connect()
    yield
    clickhouse_pool.close_connection()
    logger.info("Stopping")


app = FastAPI(title="FastAPU, Clickhouse & WebSocket", lifespan=lifespan)


@app.middleware("http")
async def log_middleware(request: Request, call_next):
    start_time = time()
    response = await call_next(request)
    total_time = time() - start_time
    logger.info(msg=f"Finished url={request.url.path} time_taken={total_time}")
    return response


app.add_middleware(
    CORSMiddleware,
    **{
        "allow_origins": [],  # list of allowed origins
        "allow_credentials": True,
        "allow_methods": ["*"],  # ["GET", "POST"] if you want to restrict
        "allow_headers": ["*"],  # ["Authorization", "Content-Type"] if restricted)
    },
)


app.include_router(router=routers, prefix="/api/v1")
