from contextlib import contextmanager
from typing import AsyncGenerator, Iterator, Any
from sqlalchemy import create_engine, schema
from sqlalchemy.orm import (
    declarative_base,
    sessionmaker,
    scoped_session,
    Session,
)
from server.config.app_configs import app_configs
from redis import Redis as SyncRedis
from redis.asyncio import Redis
from dotenv import load_dotenv
import os

load_dotenv()

# for ci testing
environment = os.getenv("ENV", "test")

engine = (
    create_engine(
        app_configs.DB.TEST_DATABASE,
    )
    if environment == "test"
    else create_engine(
        app_configs.DB.DATABASE_URL,
        pool_size=10,
        max_overflow=5,
        pool_recycle=3600,
        isolation_level="READ COMMITTED",
    )
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = (
    declarative_base()
    if environment == "test"
    else declarative_base(
        metadata=schema.MetaData(schema=app_configs.DB.SCHEMA)
    )
)
Base.query = scoped_session(SessionLocal).query_property()


@contextmanager
def get_db() -> Iterator[Session]:
    try:
        db: Session = SessionLocal()
        yield db
    except Exception as e:
        raise e
    finally:
        db.expire_on_commit
        db.close()


class RedisStorage:
    def __init__(self, host: str, port: int, db: int) -> None:
        self.redis = self.get_redis(host, port, db)
        self.async_redis = None

    def get_redis(self, host: str, port: int, db: int) -> SyncRedis:
        """Get a synchronous Redis connection."""
        redis = SyncRedis(
            host=host,
            port=port,
            db=db,
            decode_responses=True,
        )
        return redis

    async def get_async_redis(self, host: str, port: int, db: int) -> Redis:
        """Get an asynchronous Redis connection."""
        if self.async_redis is None:
            self.async_redis = Redis(
                host=host,
                port=port,
                db=db,
                decode_responses=True,
            )
        return self.async_redis